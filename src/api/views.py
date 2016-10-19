# -*- coding: utf-8 -*-
# coding=utf-8

import sys

from database import api
from interface import session


from django.shortcuts import render
import json
import os
import operator
from datetime import timedelta
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

# Create your views here.


def modify_name(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')

    dict = request.POST.dict()
    for key in dict:
        file_object.writelines(key + ": " + dict[key] + "\n")
    file_object.close()
    status = api.saveQuestionaireInfo(dict)
    return JsonResponse({
        'status': status,
    })


def create_new_act(request):
    # 这里从后端get问卷id

    # 可用POST参数有
    #	act_type: 问卷类型
    #	time    : 时间
    #   user_id : 所属用户的id，int
    dict = api.createNewQuestionaire(request.GET.dict())

    return JsonResponse({
        'status': dict["status"],
        'id': dict["id"],
    })


def create_new_qst(request):
    # 这里从后端get问题id
    # 可用POST参数有：
    #	act_id:   问卷id
    #	qst_type: 问题类型
    dict = api.createNewQuestion(request.GET.dict())
    return JsonResponse({
        'status': dict["status"],
        'id': dict["id"],
    })


def info_change_act(request):
    dicts = request.POST.dict()
    output = open('info_change.txt', 'w')
    infomations=""
    for key, value in dicts.items():
        infomations += "\"%s\":\"%s\"" % (key, value)
        infomations += "\n"
    output.write(infomations)
    return JsonResponse(dict(status='ok'))


def login_act(request):
    dicts = request.POST.dict()
    output = open('log_info.txt', 'w')
    infomations = ""
    for key, value in dicts.items():
        infomations += "\"%s\":\"%s\"" % (key, value)
        infomations += "\n"
    output.write(infomations)
    username=dicts['log_username']
    password=dicts['log_password']
    if username == 'admin' and password == '123456':
        session.add_session(request, username='admin', password='123456')
    else:
        return JsonResponse(dict(status='wrong username or password'))
    return JsonResponse(dict(status='ok'))

# ---------------------------------------------------------------------------#


def operation_qst(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    Act_id = request.GET['act_id']
    Qst_id = request.GET['qst_id']
    operation = request.GET['operation']
    file_object.writelines(Act_id + "\n")
    file_object.writelines(Qst_id + "\n")
    file_object.writelines(operation + "\n")
    return JsonResponse({
        'status': 'ok',
        })


def remove_act(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    Act_id = request.GET['act_id']
    file_object.writelines(Act_id + "\n")
    return JsonResponse({
        'status': 'ok',
    })


def save_act(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    Act_id = request.GET['act_id']
    file_object.writelines("Save: " + Act_id + "\n")
    return JsonResponse({
        'status': 'ok',
    })


def publish_act(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    Act_id = request.GET['act_id']
    file_object.writelines("Publish: " + Act_id + "\n")
    return JsonResponse({
        'status': 'ok',
    })


def modify_qst(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt' , 'w')

    dict = request.POST.dict()
    for key in dict:
        file_object.writelines(key + ": " + dict[key] + "\n")
    file_object.close()
    return JsonResponse({
            'status': 'ok',
        })


def create_new_notice(request):
	# 这里从后端get问卷id

	# 可用POST参数有
	#	act_type: 问卷类型
	#	time    : 时间
	#   user_id : 所属用户的id，int
	#dict = api.createNewQuestionaire(request.GET.dict())
	Act_id = request.GET['time']
	return JsonResponse({
		'status': "ok",
		'id': Act_id,
	})

