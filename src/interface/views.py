# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from django.shortcuts import render
import json
from datetime import timedelta
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
import session
from database import backend

# Create your views here.
def student(request):
    return render(request, 'student/index.html')


def legalUser(request):
    return legalUser_dashboard(request)

def legalUser_dashboard(request):
    #pending_applications = backend.get_pending_applications()
    #pending_count = pending_applications.count()

    #show_all_pending_applications = False
    #if pending_count > 10:
    #    show_all_pending_applications = True
    #    pending_applications = pending_applications[0:10]
    #
    #official_accounts = backend.get_official_accounts().order_by('-wci')[0:10]
    #
    #articles_count, articles = backend.get_articles(sortby=SortBy.Views, filter={
    #    'posttime_begin': timezone.now().date() - timedelta(days=7)
    #})
    #
    #category = MessageCategory.ToAdmin
    #
    #unprocessed_account = backend.get_official_accounts_with_unprocessed_messages(category)
    #
    #announcement = backend.get_announcement()

    articles = []
    official_accounts = []
    category = []
    articles_count = 0
    show_all_pending_applications = False
    unprocessed_account = []
    announcement = []
    pending_applications = []

   # return render_ajax(request, 'legalUser/dashboard.html', {
   #     'pending_applications': pending_applications,
   #     'official_accounts': official_accounts,
   #     'articles': articles,
   #     'articles_count': articles_count,
   #     'unprocessed_account': unprocessed_account,
   #     'category': category,
   #     'announcement': announcement,
   #     'show_all_pending_applications': show_all_pending_applications
   # }, 'dashboard-item')
    return render(request, 'legalUser/dashboard.html')


def test(request):
    return HttpResponse("Hello")

def render_ajax(request, url, params, item_id=''):
    if request.is_ajax():
        url = '.'.join(url.split('.')[:-1]) + '.ajax.html'
    else:
        identity = session.get_identity(request)
        name = get_realname(request)
        params['username'] = name
        if item_id != '':
            params['active_item'] = item_id
        if identity == 'admin':
            params['pending_applications_count'] = len(backend.get_pending_applications())
        elif identity == 'student':
            username = session.get_username(request)
            applications = backend.get_applications_by_user(username)
            official_accounts = applications.filter(status__exact='approved')
            params['official_accounts'] = official_accounts

    return render(request, url, params)


def get_realname(request):
    username = session.get_username(request)
    identity = session.get_identity(request)
    if identity == 'student':
        realname = backend.get_student_by_id(username).real_name
    else:
        realname = username
    return realname