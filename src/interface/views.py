# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from django.shortcuts import render
import json
import operator
import os
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
from api import views
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from send_email import send_html_mail

# Create your views here.


def check_identity(identity):
    def check_identity_func(func):
        def check(request, *args, **kw):
            if session.get_identity(request) != identity:
                if request.is_ajax():
                    return HttpResponseForbidden()
                else:
                    return HttpResponseRedirect('/legalUser/logoff/')
            return func(request, *args, **kw)
        return check
    return check_identity_func


def test(request):
    return HttpResponse("new")


@check_identity('legalUser')
def legalUser(request):
    return legalUser_dashboard(request)


@check_identity('legalUser')
def legalUser_dashboard(request):

    username = session.get_username(request)

    pending_applications = views.get_questionnaire_bySTATUS('pending', username)
    pending_count = len(pending_applications)

    show_all_pending_applications = False
    if pending_count > 10:
        show_all_pending_applications = True
        pending_applications = pending_applications[0:10]

    official_accounts = _database.get_official_accounts()

    activities = views.get_questionnaire_bySTATUS('already', username)
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


@check_identity('legalUser')
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


@check_identity('legalUser')
def legalUser_show_applications_list(request, type):
    username = session.get_username(request)
    applications = views.get_questionnaire_bySTATUS('all', username)
    return render_sortable(request, applications,
                           'legalUser/applications/applications_content.html', {
                               'type': type
                           })


@check_identity('legalUser')
def legalUser_design(request, type, act_id):
    
    act_info = views.get_questionnaire_byID(act_id)

    if act_info['act_status'] == 'pending':
        type = act_info['act_type'] 

    if type == 'enroll':
        type_name = u'报名/统计表'
        type_icon = 'fa-tasks'
    elif type == 'recruit':
        type_name = u'实验室招募'
        type_icon = 'fa-calendar-check-o'
    elif type == 'vote':
        type_name = u'投票'
        type_icon = 'fa-list-alt'
    item_id = type + '-design-item'
    return render_ajax(request, 'legalUser/design/design.html', {
        'type': type,
        'design_type': type_name,
        'design_icon': type_icon,
        'act_id': act_id,
        'act_info': act_info
    }, item_id)


def legalUser_design_question(request, type, act_id):
    question_url = 'legalUser/design/questions/' + request.GET.get('questions_type') + '.html'
    statistics = views.get_statistics_of_question(request.GET.get('questions_id'))
    params = {}
    params = {
        'questions_type': request.GET.get('questions_type'),
        'questions_title': request.GET.get('questions_title'),
        'questions_id': request.GET.get('questions_id'),
        'option_num': request.GET.get('option_num'),
        'option': request.GET.get('option'),
        'rows': request.GET.get('rows'),
        'hint': request.GET.get('hint'),

        'qst_must': request.GET.get('qst_must'),
        'min_selected': request.GET.get('min_selected'),
        'max_selected': request.GET.get('max_selected'),

        'display_vote': request.GET.get('display_vote'),
        'ip_times': request.GET.get('ip_times'),
        'day_times': request.GET.get('day_times'),
        'statistics': statistics
    }
    params['act_type'] = type
    params['act_id'] = act_id
    return render(request, question_url, params)


def show_modal(request):
    modal_type = request.GET['modal_type']
    id = request.GET['id']
    return render(request, 'legalUser/design/modal/' + modal_type + '_modal.html', {
            'qst_type': modal_type,
            'id': id,
        })


def show_info_modal(request):
    modal_type = request.GET['modal_type']
    username = request.GET['username']

    dicts = views.get_user_information_act(username)

    params = {
        'username': username,
        'real_name': dicts['real_name'],
        'identity': 'legalUser',
        'email': dicts['email'],
        'telephone_number': dicts['telephone_number'],
        'age': dicts['age'],
        'gender': dicts['gender'],
        'address': dicts['address'],
        'status': dicts['status'],
    }

    return render(request, 'legalUser/design/modal/' + modal_type + '_modal.html', params)


def log_off(request):
    session.del_session(request)
    return HttpResponseRedirect('/login/')


def login_page(request):
    if session.get_identity(request) == 'legalUser':
        return legalUser(request)
    elif session.get_identity(request) == 'manager':
        return manager(request)
    log_page_html = 'legalUser/login/log_page.html'
    return render(request, log_page_html)


@check_identity('legalUser')
def user_information(request):
    username = session.get_username(request)
    dicts = views.get_user_information_act(username)

    params = {
        'username': session.get_username(request),
        'real_name': dicts['real_name'],
        'identity': session.get_identity(request),
        'email': dicts['email'],
        'telephone_number': dicts['telephone_number'],
        'age': dicts['age'],
        'gender': dicts['gender'],
        'address': dicts['address'],
        'status': dicts['status'],
    }
    user_information_html = 'legalUser/information/user_information.html'
    return render_ajax(request, user_information_html, params, 'info-item-1')


@check_identity('legalUser')
def user_information_change(request):
    username = session.get_username(request)
    dicts = views.get_user_information_act(username)

    params = {
        'username': session.get_username(request),
        'real_name': dicts['real_name'],
        'identity': session.get_identity(request),
        'email': dicts['email'],
        'telephone_number': dicts['telephone_number'],
        'age': dicts['age'],
        'gender': dicts['gender'],
        'address': dicts['address'],
        'status': dicts['status'],
    }
    user_information_change_html = 'legalUser/information/user_information_change.html'
    return render_ajax(request, user_information_change_html, params, 'info-item-2')


def guest(request):
    session.del_session(request)
    session.add_session(request, identity='guest')
    return guest_dashboard(request)


@check_identity('guest')
def guest_dashboard(request):
    username = session.get_username(request)

    pending_applications = views.get_questionnaire_bySTATUS('pending', username)
    pending_count = len(pending_applications)

    show_all_pending_applications = False
    if pending_count > 10:
        show_all_pending_applications = True
        pending_applications = pending_applications[0:10]

    official_accounts = _database.get_official_accounts()

    activities = views.get_questionnaire_bySTATUS('already', username)
    articles_count = len(activities)

    # category = MessageCategory.ToAdmin

    unprocessed_account = _database.get_official_accounts_with_unprocessed_messages()

    announcement = _database.get_announcement()

    category = 1

    return render_ajax(request, 'guest/dashboard_guest.html', {
        'pending_applications': pending_applications,
        'official_accounts': official_accounts,
        'activities': activities,
        'articles_count': articles_count,
        'unprocessed_account': unprocessed_account,
        'category': category,
        'announcement': announcement,
        'show_all_pending_applications': show_all_pending_applications
    }, 'dashboard-item')


@check_identity('guest')
def guest_design(request, type, act_id):

    act_info = views.get_questionnaire_byID(act_id)

    if act_info['act_status'] == 'pending':
        type = act_info['act_type']

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
    return render_ajax(request, 'guest/design/design.html', {
        'type': type,
        'design_type': type_name,
        'design_icon': type_icon,
        'act_id': act_id,
        'act_info': act_info
    }, item_id)


@check_identity('guest')
def guest_show_applications(request, type):
    return legalUser_show_applications(request, type)


#manageUser
@check_identity('manager')
def manager(request):
    return manager_dashboard(request)


@check_identity('manager')
def manager_dashboard(request):
    username = session.get_username(request)

    pending_applications = views.get_questionnaire_bySTATUS('pending', username)
    pending_count = len(pending_applications)

    show_all_pending_applications = False
    if pending_count > 10:
        show_all_pending_applications = True
        pending_applications = pending_applications[0:10]

    official_accounts = _database.get_official_accounts()

    activities = views.get_questionnaire_bySTATUS('already', username)
    articles_count = len(activities)

    # category = MessageCategory.ToAdmin

    unprocessed_account = _database.get_official_accounts_with_unprocessed_messages()

    announcement = _database.get_announcement()

    category = 1

    return render_ajax(request, 'manager/dashboard_manager.html', {
        'pending_applications': pending_applications,
        'official_accounts': official_accounts,
        'activities': activities,
        'articles_count': articles_count,
        'unprocessed_account': unprocessed_account,
        'category': category,
        'announcement': announcement,
        'show_all_pending_applications': show_all_pending_applications
    }, 'dashboard-item')


@check_identity('manager')
def manager_all_activities(request):
    return render_ajax(request, 'manager/application/applications.html', {}, 'all-questionnaire-item')


@check_identity('manager')
def manager_all_activities_list(request):
    applications = views.get_all_questionnaire()
    for app in applications:
        app['publisher'] = app['username']
    output = open('asdfasdfasdfasd', 'w')
    output.write(str(len(applications)))
    output.close()
    return render_sortable(request, applications, 'manager/application/applications_content.html')


@check_identity('manager')
def manager_all_users(request):
    return render_ajax(request, 'manager/application_2/applications.html', {}, 'all-users-item')


@check_identity('manager')
def manager_all_users_list(request):
    applications = views.get_all_user()
    for app in applications:
        app['name'] = app['username']
    return render_sortable(request, applications, 'manager/application_2/applications_content.html')


@check_identity('manager')
def manager_notice(request):
    params = {'notice': '这里是管理员发布的公告'}
    return render_ajax(request, 'manager/notice/manager_notice.html', params, 'notice-design-item')


#statistics
@check_identity('legalUser')
def show_statistics_choose(request):
    username = session.get_username(request)
    activities = views.get_questionnaire_bySTATUS('already', username)
    return render_ajax(request, 'legalUser/statistics/statistics_choose.html', {
        'activities': activities
    }, 'statistics-list-item')


@check_identity('legalUser')
def show_statistics(request, act_id):
    act_info = views.get_questionnaire_byID(act_id)
    applications = views.get_participants(act_id)
    
    for fillin in applications:
        toAppend = []
        for qst in act_info['questions']:
            fillin_id = fillin['id']
            qst_id = qst['qst_id']
            qst_info = views.get_result_of_question(act_id, qst_id, fillin_id)
            toAppend.append(qst_info)
        fillin['fillin_result'] = toAppend

    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    for fillin in applications:
        for key in fillin:
            file_object.writelines(key + ': ' + str(fillin[key]) + '\n')
        file_object.writelines('\n')

    return render_ajax(request, 'legalUser/statistics/statistics.html', {
        'act_id': act_id,
        'act_info': act_info,
        'item':applications,
    }, 'statistics-list-item')


def show_charts(request, act_id, qst_id):
    tableData = {}
    tableData['column_chart'] = views.get_columnChart_json(act_id, qst_id)
    tableData['pie_chart'] = views.get_pieChart_json(act_id, qst_id)
    tableData['bar_chart'] = views.get_barChart_json(act_id, qst_id)
    tableData['circle_chart'] = views.get_circleChart_json(act_id, qst_id)
    return render(request, 'legalUser/statistics/charts/charts.html',{
            'tableData': tableData
        })

def guest_statistics(request, act_id):
    act_info = views.get_questionnaire_byID(act_id)
    applications = views.get_participants(act_id)
    
    for fillin in applications:
        toAppend = []
        for qst in act_info['questions']:
            fillin_id = fillin['id']
            qst_id = qst['qst_id']
            qst_info = views.get_result_of_question(act_id, qst_id, fillin_id)
            toAppend.append(qst_info)
        fillin['fillin_result'] = toAppend

    return render(request, 'publish/management/index.html', {
        'act_id': act_id,
        'act_info': act_info,
        'item':applications
    })


def show_participants_list(request, act_id):
    applications = views.get_participants(act_id)
    return render_sortable(request, applications,
                           'legalUser/statistics/participants/participants_content.html', {
                               'act_id': act_id
                           })


def statistics_question(request, act_id):
    question_url = 'legalUser/statistics/questions/' + request.GET.get('questions_type') + '/' + request.GET.get('questions_type') + '_list.html'
    params = {}
    params = {
        'questions_type': request.GET.get('questions_type'),
        'questions_title': request.GET.get('questions_title'),
        'questions_id': request.GET.get('questions_id'),
        }
    params['act_type'] = type
    params['act_id'] = act_id
    return render(request, question_url, params)


def statistics_question_list(request, act_id, qst_type, qst_id):
    question_url = 'legalUser/statistics/questions/' + qst_type + '/' + qst_type + '_content.html'
    applications = views.get_statistics_of_question(qst_id)
    return render_sortable(request, applications, question_url, {
            'act_id': act_id
        })


#questionnaire
def questionnaire_publish_question(request, type, act_id):
    question_url = 'questionnaire/publish_qst/' + request.GET.get('questions_type') + '.html'
    statistics = views.get_statistics_of_question(request.GET.get('questions_id'))
    params = {}
    params = {
        'questions_type': request.GET.get('questions_type'),
        'questions_title': request.GET.get('questions_title'),
        'questions_id': request.GET.get('questions_id'),
        'option_num': request.GET.get('option_num'),
        'option': request.GET.get('option'),
        'rows': request.GET.get('rows'),
        'hint': request.GET.get('hint'),

        'statistics': statistics,

        'qst_must': request.GET.get('qst_must'),
        'min_selected': request.GET.get('min_selected'),
        'max_selected': request.GET.get('max_selected'),

        'fillin_id': request.GET.get('fillin_id'),

        'display_vote': request.GET.get('display_vote'),
        'ip_times': request.GET.get('ip_times'),
        'day_times': request.GET.get('day_times')
    }
    if request.GET.get('fillin_id') != None and request.GET.get('fillin_id') != '':
        fillin_result = views.get_result_of_question(act_id, request.GET.get('questions_id'), request.GET.get('fillin_id'))
        params['result'] = fillin_result



    params['act_type'] = type
    params['act_id'] = act_id
    return render(request, question_url, params)


def questionnaire(request, act_id):
    act_info = views.get_questionnaire_byID(act_id)

    status = act_info['act_status']
    if status == 'already':
        type = act_info['act_type']
    else:
        if status == 'pending':
            return render_ajax(request, 'questionnaire/err_visit.html', {
                'qst_status': "问卷未发布"})
        elif status == 'pause':
            return render_ajax(request, 'questionnaire/err_visit.html', {
                'qst_status': "问卷已截止"})
        else:
            return render_ajax(request, 'questionnaire/err_visit.html', {
                'qst_status': "问卷不存在"})

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

    return render_ajax(request, 'questionnaire/questionnaire.html', {
        'type': type,
        'act_id': act_id,
        'act_info': act_info
    }, item_id)


def fillin_questionnaire(request, act_id, fillin_id):
    act_info = views.get_questionnaire_byID(act_id)

    return render(request, 'questionnaire/questionnaire.html', {
        'act_id': '1000',
        'act_info': act_info,
        'fillin_id': fillin_id,
        'type': 'pending'
    })


def fill_in_success(request):
    return render(request, 'questionnaire/questionnaire_success.html')


#----------------------------分割线--------------------------------#

def render_ajax(request, url, params, item_id=''):
    if request.is_ajax():
        url = '.'.join(url.split('.')[:-1]) + '.ajax.html'
    else:
        identity = session.get_identity(request)
        name = get_realname(request)
        if identity == 'legalUser':
            params['username'] = session.get_username(request)
        elif identity == 'guest':
            params['username'] = "游客"
        elif identity == 'manager':
            params['username'] = "管理员"
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
        u'asc': False,
        u'desc': True
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
        for key in item:
            if search_keyword in str(item[key]):
                modify_items.append(item)
                break

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


def get_username(request):
    username = session.get_username(request)
    user_id = session.get_student_id(request)
    file_object = open(os.path.abspath('.') + '/interface/stat_database.txt' , 'w')
    file_object.writelines(username + "\n")
    if username == 'none' or user_id == 'none':
        return JsonResponse({
            'status': 'wrong',
        })
    else:
        return JsonResponse({
            'status': 'OK',
            'username': username,
            'user_id' : user_id,
        })
