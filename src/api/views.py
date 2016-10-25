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

from interface import _database

# Create your views here.


def modify_name(request):
	#issue closed
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt' , 'w')

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
	#可用POST参数有 
	#	act_type: 问卷类型
	#	time    : 时间  
	#   user_id : 所属用户的id，int

	#issue closed
	dict = api.createNewQuestionaire(request.GET.dict())
	
	return JsonResponse({
			'status': dict["status"],
			'id': dict["id"],
		})


def create_new_qst(request):
	#这里从后端get问题id
	#可用POST参数有：
	#	act_id:   问卷id
	#	qst_type: 问题类型

	
	dict = api.createNewQuestion(request.GET.dict())
	return JsonResponse({
			'status': dict["status"],
			'id': dict["id"],
		})

# ---------------------------------------------------------------------------#


def operation_qst(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    Act_id = request.GET['act_id']
    Qst_id = request.GET['qst_id']
    operation = request.GET['operation']
    file_object.writelines(Act_id + "\n")
    file_object.writelines(Qst_id + "\n")
    file_object.writelines(operation + "\n")
    status = api.operateQuestion(request.GET.dict())
    return JsonResponse({
        'status': status,
    })


def remove_act(request):
	file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
	Act_id = request.GET['act_id']
	file_object.writelines(Act_id + "\n")
	status = api.deleteQuestionaire(request.GET.dict())
	return JsonResponse({
			'status': status,
		})


def save_act(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    Act_id = request.GET['act_id']
    file_object.writelines("Save: " + Act_id + "\n")
    status = api.saveQuestionaire(request.GET.dict())
    return JsonResponse({
        'status': status,
    })


def publish_act(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    Act_id = request.GET['act_id']
    file_object.writelines("Publish: " + Act_id + "\n")
    status = api.publishQuestionaire(request.GET.dict())
    return JsonResponse({
        'status': status,
    })

#--------------------------------------------------------------------------------------#

def modify_qst(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt' , 'w')

    dict = request.POST.dict()
    for key in dict:
        file_object.writelines(key + ": " + dict[key] + "\n")
    file_object.close()
    status = api.modifyQuestion(dict)
    return JsonResponse({
            'status': status,
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
    information = ""
    for key, value in dicts.items():
        information += "\"%s\":\"%s\"" % (key, value)
        information += "\n"
    output.write(information)
    username = dicts['log_username']
    password = dicts['log_password']
    if username == 'admin' and password == '123456':
        identity = 'legalUser'
        session.add_session(request, username=username, identity=identity)
    elif username == 'manager' and password == '123456':
        identity = 'manager'
        session.add_session(request, username=username, identity=identity)
    else:
        return JsonResponse(dict(status='wrong username or password'))
    return JsonResponse(dict(status='ok', identity=identity))


def get_questionnaire_byID(act_id):
	#act_id:问卷id
	result = _database.get_questionnaire_byID(act_id)
	return result

def get_questionnaire_bySTATUS(status, username):
    #status: 问卷状态
    #username: 用户名
    dict = {
        "status" : status,
        "username" : username
    }
    result = api.getQuestionaireListByStatus(dict)
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt' , 'w')

    
    for item in result:
        for key in item:
            file_object.writelines(key + ": " + str(item[key]) + "\n")
        
        if item['status'] == 'already':
            item['status_display'] = {
                 'colorclass': 'success',
                 'icon': 'fa-check',
                 'name': u'已发布'
             }
        elif item['status'] == 'pending':
            item['status_display'] = {
                    'colorclass': 'warning',
                    'icon': 'fa-cogs',
                    'name': u'待发布'
                 }
        file_object.writelines("\n")
    file_object.close()
#   if status == 'pending':
#       result = _database.get_pending_applications()
#   elif status == 'already':
#       result = _database.get_already_applications()
#   elif status == 'all':
#       result = _database.get_all_applications()
    return result

def get_participants(act_id):
    #act_id: 问卷id
    result = _database.get_participants()
    return result

def get_result_of_question(act_id, qst_id, fillin_id):
    #act_id: 问卷id
    #qst_id: 问题id
    #fillin_id: 填写id
    result = _database.get_result_of_question(act_id, qst_id, fillin_id)
    return result
