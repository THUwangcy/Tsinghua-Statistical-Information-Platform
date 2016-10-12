# -*- coding: utf-8 -*-
# coding=utf-8

import sys
sys.path.append("..")


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
from interface import session
from interface import _database

from database import api

# Create your views here.

def modify_name(request):
	file_object = open(os.path.abspath('.') + '/interface/static_database.txt' , 'w')

	dict = request.POST.dict()
	for key in dict:
		file_object.writelines(key + ": " + dict[key] + "\n")
	file_object.close()
	status = saveQuestionaireInfo(dict)
	return JsonResponse({
			'status': status,
		})


def create_new_act(request):
	#这里从后端get问卷id

	#可用POST参数有 
	#	act_type: 问卷类型
	#	time    : 时间
	dict = createNewQuestionaire(request.POST.dict())
	
	return JsonResponse({
			'status': dict["status"],
			'id': dict["id"],
		})


def create_new_qst(request):
	#这里从后端get问题id
	
	#可用POST参数有：
	#	act_id:   问卷id
	#	qst_type: 问题类型
	dict = createNewQuestion(request.POST.dict())
	return JsonResponse({
			'status': dict["status"],
			'id': dict["id"],
		})
	
