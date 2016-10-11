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

# Create your views here.

def modify_something(request, modal_type):
	file_object = open(os.path.abspath('.') + '/interface/static_database.txt' , 'w')
	content_list = ['测试修改\n',
					'2016.10.01\n',
					'pending\n',
					'1235\n',
					'已修改\n',
					'warning\n',
					'fa-cogs\n',
					'待发布\n']
	for line in content_list:
		file_object.writelines(line)
	file_object.close()
	return HttpResponse("ok")
	
