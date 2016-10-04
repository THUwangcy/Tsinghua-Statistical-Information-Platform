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
import _database
from database import backend

# Create your views here.
def student(request):
    return render(request, 'student/index.html')


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

    activities = _database.get_activities()
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


def test(request):
    return HttpResponse("Hello")

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