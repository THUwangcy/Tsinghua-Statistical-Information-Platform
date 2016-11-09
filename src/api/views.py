# -*- coding: utf-8 -*-
# coding=utf-8

import sys

from database import api
from interface import session

import re

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
from interface import send_email

import urllib
import urllib2
import thread

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
    act_id = request.GET['act_id']

    content = {}
    try:
        questionnaire_url = request.GET['questionnaire_url']
        manage_url = request.GET['management_url']
        content = {
            'email': session.get_email(request),
            'manage_url': manage_url,
            'questionnaire_url': questionnaire_url,
        }
    except:
        pass

    try:
        thread.start_new_thread(send_email.send_html_mail, ("来自清华大学信息化统计平台", content, [session.get_email(request), ], ))
        # send_email.send_html_mail("来自清华大学信息化统计平台", content, [session.get_email(request), ])
    except:
        pass

    file_object.writelines("Publish: " + act_id + "\n")
    status = api.publishQuestionaire(request.GET.dict())

    session.del_email(request)
    return JsonResponse({
        'status': status,
    })


def register_email(request):
    dicts = request.POST.dict()
    email = dicts['email']
    session.add_session(request, email=email)
    return JsonResponse({
        'status': 'ok',
    })

#--------------------------------------------------------------------------------------#

def modify_qst(request):
    file_object = open(os.path.abspath('.') + '/interface/stat_database.txt' , 'w')

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
    username = dicts['log_username']
    password = dicts['log_password']
    if username == 'manager' and password == '123456':
        identity = 'manager'
        session.add_session(request, username=username, identity=identity)
    elif username == 'admin' and password == '123456':
        identity = 'legalUser'
        session.add_session(request, username=username, identity=identity)
    else:
        data = {
            'id': username,
            'pw': password,
        }
        url = 'http://student.tsinghua.edu.cn/api/temp_login'
        post_data = urllib.urlencode(data)

        req = urllib2.urlopen(url, post_data)
        content = req.read()

        user_data = {}

        try:
            user = json.loads(content)
            user_data['yhm'] = user['yhm']
            user_data['xm'] = user['xm']
            user_data['zjh'] = user['zjh']
            user_data['email'] = user['email']
            identity = 'legalUser'
            session.add_session(request, username=user_data['yhm'], identity=identity)
        except:
            return JsonResponse(dict(status='wrong username or password'))
    return JsonResponse(dict(status='ok', identity=identity))



def get_questionnaire_byID(act_id):
	#act_id:问卷id
    result = api.getQuestionaireByID(act_id)
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt' , 'w')

    for item in result:
        file_object.writelines(item + ": " + str(result[item]) + "\n")
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
    file_object.writelines("username: " + username)
    
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
        elif item['status'] == 'pause':
            item['status_display'] = {
                    'colorclass': 'danger',
                    'icon': 'fa-pause',
                    'name': u'已暂停'
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
    result = api.getFillers(act_id)
    return result

def get_result_of_question(act_id, qst_id, fillin_id):
    #act_id: 问卷id
    #qst_id: 问题id
    #fillin_id: 填写id
    result = api.getQuestionFill(act_id, qst_id, fillin_id)
    return result


def get_statistics_of_question(qst_id):
    #qst_id: 问题id 获取该问题的详细统计信息
    result = api.getStatisticsOfQuestion(qst_id)
    return result


def notice_act(request):
    dicts = request.POST.dict()
    return JsonResponse(dict(status='ok'))

#问卷提交函数 目前已实现 单选、填空
#格式infomations如下
#"qst1":"option1"
#"qst2":"sss"
#"act_id":"3"
#"csrfmiddlewaretoken":"As64oYUOYYDSsz3FfW6PWM8Ku89kpgaD"
def questionnaire_submit(request):

    dicts = request.POST.dict()
    output = open('questionnaire2.txt', 'w')
    infomations2 = {}
    pattern = 'option'
    regex = re.compile(pattern)
    for key, value in dicts.items():
        match = regex.search(value)
        if match:
            result_list = request.POST.getlist(key, '')
            infomations2[key] = result_list
        else:
            infomations2[key]=value

    for key in infomations2:
        output.writelines(str(key) + ": " + str(infomations2[key]) + '\n')
 #   output.write(infomations2)
    status = api.fillQuestionaire(infomations2)

    return JsonResponse(dict(status='ok'))

def stop_act(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    Act_id = request.GET['act_id']
    file_object.writelines("Stop: " + Act_id + "\n")
    status = 'ok'
    return JsonResponse({
        'status': status,
    })

def resume_act(request):
    file_object = open(os.path.abspath('.') + '/interface/static_database.txt', 'w')
    Act_id = request.GET['act_id']
    file_object.writelines("Resume: " + Act_id + "\n")
    status = 'ok'
    return JsonResponse({
        'status': status,
    })


def get_columnChart_json(act_id, qst_id):
    act_info = get_questionnaire_byID(act_id)
    question = {}
    for qst in act_info['questions']:
        if qst['qst_id'] == int(qst_id):
            question = qst
            break
    qst_info = get_statistics_of_question(qst_id)
    question['qst_info'] = qst_info
    if question['qst_type'] == 'fillin':
        return {}
    tableData = {
        'chart': {
            'caption': question['qst_title'],
            'subCaption': question['qst_type'],
            'xAxisName': '选项',
            'pYAxisName': '选择人数',
            'sYAxisName': '百分比',
            'sYAxisMaxValue': 150,
            'pYAxisMaxValue': 0
        },
        'categories': [
            {
                'category': []
            }
        ],
        'dataset': [
            {
                'seriesName': '选择人数',
                'data': []
            },
            {
                'seriesName': '百分比',
                'parentYAxis': 'S',
                'renderAs': 'area',
                'data': []
            }
        ]
    }

    for option in question['option']:
        tableData['categories'][0]['category'].append({
            'label': str(option)
        })
    for option in question['qst_info']:
        tableData['dataset'][0]['data'].append({
            'value': str(option['count'])
        })
        tableData['dataset'][1]['data'].append({
            'value': str(option['percentage'])
        })

    if question['qst_type'] == 'single':
        tableData['chart']['subCaption'] = u'单选题'
    elif question['qst_type'] == 'multi':
        tableData['chart']['subCaption'] = u'多选题'
    elif question['qst_type'] == 'mark':
        tableData['chart']['subCaption'] = u'招募题'
    else:
        tableData = {}

    tableData = json.dumps(tableData)
    return tableData


def get_pieChart_json(act_id, qst_id):
    act_info = get_questionnaire_byID(act_id)
    question = {}
    for qst in act_info['questions']:
        if qst['qst_id'] == int(qst_id):
            question = qst
            break
    qst_info = get_statistics_of_question(qst_id)
    question['qst_info'] = qst_info

    if question['qst_type'] == 'fillin':
        return {}

    tableData = {
        'chart': {
            'caption': question['qst_title'],
            'subCaption': question['qst_type'],
            'showLegend': '1',
            'legendItemFontSize': '12',
            "startingAngle": "310",
        },
        'data': []
    }

    for option in question['qst_info']:
        tableData['data'].append({
                'label': option['content'],
                'value': option['count']
            })

    if question['qst_type'] == 'single':
        tableData['chart']['subCaption'] = u'单选题'
    elif question['qst_type'] == 'multi':
        tableData['chart']['subCaption'] = u'多选题'
    elif question['qst_type'] == 'mark':
        tableData['chart']['subCaption'] = u'招募题'
    else:
        tableData = {}

    tableData = json.dumps(tableData)
    return tableData


def get_barChart_json(act_id, qst_id):
    act_info = get_questionnaire_byID(act_id)
    question = {}
    for qst in act_info['questions']:
        if qst['qst_id'] == int(qst_id):
            question = qst
            break
    qst_info = get_statistics_of_question(qst_id)
    question['qst_info'] = qst_info

    if question['qst_type'] == 'fillin':
        return {}

    tableData = {
        'chart': {
            'caption': question['qst_title'],
            'subCaption': question['qst_type'],
            "yAxisName": u"选择人数",
        },
        'data': []
    }

    for option in question['qst_info']:
        tableData['data'].append({
                'label': option['content'],
                'value': option['count']
            })
    if question['qst_type'] == 'single':
        tableData['chart']['subCaption'] = u'单选题'
    elif question['qst_type'] == 'multi':
        tableData['chart']['subCaption'] = u'多选题'
    elif question['qst_type'] == 'mark':
        tableData['chart']['subCaption'] = u'招募题'
    else:
        tableData = {}

    tableData = json.dumps(tableData)
    return tableData


def get_circleChart_json(act_id, qst_id):
    act_info = get_questionnaire_byID(act_id)
    question = {}
    for qst in act_info['questions']:
        if qst['qst_id'] == int(qst_id):
            question = qst
            break
    qst_info = get_statistics_of_question(qst_id)
    question['qst_info'] = qst_info
    if question['qst_type'] == 'fillin':
        return {}
    tableData = {
        'chart': {
            'caption': question['qst_title'],
            'subCaption': question['qst_type'],
            "showBorder": "0",
            "use3DLighting": "0",
            "enableSmartLabels": "0",
            "startingAngle": "310",
            "showLabels": "0",
            "showPercentValues": "1",
            "showLegend": "1",
            "defaultCenterLabel": "总填写人数: " + str(question['qst_info'][0]['total']),
            "centerLabel": "Option situation: $label: $value",
            "centerLabelBold": "1",
            "showTooltip": "0",
            "decimals": "0",
            "useDataPlotColorForLabels": "1",
            "theme": "fint"
        },
        'data': []
    }

    for option in question['qst_info']:
        tableData['data'].append({
                'label': option['content'],
                'value': option['count']
            })
    if question['qst_type'] == 'single':
        tableData['chart']['subCaption'] = u'单选题'
    elif question['qst_type'] == 'multi':
        tableData['chart']['subCaption'] = u'多选题'
    elif question['qst_type'] == 'mark':
        tableData['chart']['subCaption'] = u'招募题'
    else:
        tableData = {}

    tableData = json.dumps(tableData)
    return tableData