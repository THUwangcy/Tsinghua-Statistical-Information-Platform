# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from django.shortcuts import render
import json
import operator
from datetime import timedelta
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
import session
import _database
from database import backend

# Create your views here.

def test(request):
    return HttpResponse("new")


def legalUser(request):
    return legalUser_dashboard(request)

def legalUser_dashboard(request):
    pending_applications = _database.get_pending_applications()
    pending_count = len(pending_applications)

    show_all_pending_applications = False
    if pending_count > 10:
        show_all_pending_applications = True
        pending_applications = pending_applications[0:10]

    official_accounts = _database.get_official_accounts()

    activities = _database.get_already_applications()
    articles_count = len(activities)

    #category = MessageCategory.ToAdmin

    unprocessed_account = _database.get_official_accounts_with_unprocessed_messages()

    announcement = _database.get_announcement()


    category = 1

    return render_ajax(request, 'legalUser/dashboard.html', {
        'pending_applications': pending_applications,
        'official_accounts': official_accounts,
        'activities': activities,
        'articles_count': articles_count,
        'unprocessed_account': unprocessed_account,
        'category': category,
        'announcement': announcement,
        'show_all_pending_applications': show_all_pending_applications
    }, 'dashboard-item')


def legalUser_show_applications(request, type):
    if type == 'pending':
        type_name = u'待发布报名'
        type_icon = 'fa-tasks'
    elif type == 'already':
        type_name = u'我发布的报名'
        type_icon = 'fa-check'
    elif type == 'all':
        type_name = u'所有报名'
        type_icon = 'fa-th-list'
    elif type == 'trash':
        type_name = u'已删除报名'
        type_icon = 'fa-trash'
    else:
        type_name = ''
        type_icon = ''
    item_id = type + '-applications-item'

    return render_ajax(request, 'legalUser/applications/applications.html', {
        'type': type,
        'application_type': type_name,
        'application_icon': type_icon
    }, item_id)


def legalUser_show_applications_list(request, type):
    applications = _database.get_all_applications()
    return render_sortable(request, applications,
                           'legalUser/applications/applications_content.html', {
                               'type': type
                           })


def legalUser_design(request, type):
    if type == 'enroll':
        type_name = u'报名/统计表'
        type_icon = 'fa-tasks'
    elif type == 'recruit':
        type_name = u'实验室招募'
        type_icon = 'fa-check'
    elif type == 'vote':
        type_name = u'投票'
        type_icon = 'fa-list-alt'
    item_id = type + '-design-item'
    return render_ajax(request, 'legalUser/design/design.html', {
        'type': type,
        'design_type': type_name,
        'design_icon': type_icon
    }, item_id)


def legalUser_design_question(request, type):
    question_url = 'legalUser/design/questions/' + request.GET.get('questions_type') + '.html'
    return render(request, question_url)




def render_ajax(request, url, params, item_id=''):
    if request.is_ajax():
        url = '.'.join(url.split('.')[:-1]) + '.ajax.html'
    else:
        identity = session.get_identity(request)
        name = get_realname(request)
        params['username'] = "王晨阳"
        if item_id != '':
            params['active_item'] = item_id
        if identity == 'admin':
            params['pending_applications_count'] = len(_database.get_pending_applications())
        elif identity == 'student':
            username = session.get_username(request)
            applications = backend.get_applications_by_user(username)
            official_accounts = applications.filter(status__exact='approved')
            params['official_accounts'] = official_accounts

    return render(request, url, params)


def render_sortable(request, items, url, params=None):
    #这里来的request是调用loadContent系列函数时传的，里面有各种param
    if not params:
        params = {}
    items_per_page = params.pop("items_per_page", 10)

    page_current = int(request.GET.get('page', '1'))

    sort_order_keyword = request.GET.get('sort_order', 'desc')
    #sort_order_keyword为desc时对sort_by_keyword取负
    sort_order = {
        'asc': False,
        'desc': True
    }[sort_order_keyword]

    sort_by_keyword = request.GET.get('sort_by', '')

    set_filter = {}
    search_keyword = request.GET.get('search_keyword', '').strip()
    search_field = request.GET.get('search_field')
    if search_field and search_keyword:
        set_filter[search_field + '__contains'] = search_keyword

    start_from = (page_current - 1) * items_per_page

    #该句实现排序和搜索，根据sort_order和sort_by_keyword
    #items = items.filter(**set_filter).order_by(sort_order + sort_by_keyword)

    #search操作，今后要在数据库中
    modify_items = []
    for item in items:
        if search_keyword in item['name'] or search_keyword in item['description']:
            modify_items.append(item)

    items = modify_items

    #排序操作
    items = sorted(items, key = operator.itemgetter(sort_by_keyword), reverse = sort_order)

    item_count = len(items)
    items = items[start_from:(start_from + items_per_page)]

    page = get_pagination(item_count, items_per_page, page_current)

    return render(request, url, {
        'items': items,
        'item_count': item_count,
        'page': page,
        'sort_by': sort_by_keyword,
        'sort_order': sort_order_keyword,
        'params': params
    })


def get_realname(request):
    username = session.get_username(request)
    identity = session.get_identity(request)
    if identity == 'student':
        realname = backend.get_student_by_id(username).real_name
    else:
        realname = username
    return realname


def get_pagination(item_total, item_per_page, cur):
    page_count = (item_total + item_per_page - 1) // item_per_page

    l = max(1, cur - 1)
    r = min(page_count, cur + 2)
    if l <= 2:
        l = 1
    if r >= page_count - 1:
        r = page_count
    pages = xrange(l, r + 1)
    page = {'count': page_count,
            'current': cur,
            'pages': pages}
    return page


def login_page(request):
    log_page_html = 'legalUser/log_page.html'
    return render(request, log_page_html)


def user_information(request):
    identity = session.get_identity(request)
    params = {
        'username': '王晨阳'
    }
    if identity == 'admin':
        params['pending_applications_count'] = len(_database.get_pending_applications())
    elif identity == 'student':
        username = session.get_username(request)
        applications = backend.get_applications_by_user(username)
        official_accounts = applications.filter(status__exact='approved')
        params['official_accounts'] = official_accounts

    user_information_html = 'legalUser/user_information.html'
    return render(request, user_information_html, params)
