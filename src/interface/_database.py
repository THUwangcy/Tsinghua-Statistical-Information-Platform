# -*- coding: utf-8 -*-
# coding=utf-8
# encoding:utf-8

#处理中文需要
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from operator import itemgetter
import os


def get_pending_applications():
    item1 = {'name': u'诚招女友 欢迎报名',
             'subscribe_time': '2016.10.01',
             'status': 'pending',
             'id': 1235,
             'description': u'找个女朋友陪我过十一QAQ',
             'status_display': {
                'colorclass': 'warning',
                'icon': 'fa-cogs',
                'name': u'待发布'
             }
             }
    item2 = {'name': u'名字一定要长名字一定要长名字一定要长',
             'subscribe_time': '2016.10.04',
             'status': 'pending',
             'id': 1238,
             'status_display': {
                'colorclass': 'warning',
                'icon': 'fa-cogs',
                'name': u'待发布'
             },
             'description': u'你一定没见过这么标准的十五个字\n你一定没见过这么标准的十五个字\n你一定没见过这么标准的十五个字\n'
                            u'你一定没见过这么标准的十五个字\n你一定没见过这么标准的十五个字\n你一定没见过这么标准的十五个字'
             }
    item3 = {'name': u'源：厉害了我的哥',
             'subscribe_time': '2016.10.05',
             'status': 'pending',
             'id': 1274,
             'description': u'半藏：当然了我的弟',
             'status_display': {
                'colorclass': 'warning',
                'icon': 'fa-cogs',
                'name': u'待发布'
             }
             }

    file_object = open(os.path.abspath('.') + '/interface/static_database.txt' , 'r')
    item_change = {'name': file_object.readline(),
                   'subscribe_time': file_object.readline(),
                   'status': file_object.readline(),
                   'id': file_object.readline(),
                   'description': file_object.readline(),
                   'status_display': {
                        'colorclass': file_object.readline(),
                        'icon': file_object.readline(),
                        'name': file_object.readline()
                    }
                }
    file_object.close()
    return [item1, item2, item3, item_change]


def get_already_applications():
    item1 = {'subscribe_time': '2016.10.04',
             'name': u'眼动实验被试者招募',
             'id': 1234,
             'description': u'计算机系人工智能研究所搜索引擎相关实验，报酬优厚',
             'status': 'already',
             'fillin': 11232,
             'views': 343241,
             'status_display': {
                 'colorclass': 'success',
                 'icon': 'fa-check',
                 'name': u'已发布'
             }
             }
    item2 = {'subscribe_time': '2016.06.02',
             'name': u'票选你最喜欢的大腿活动',
             'id': 1234,
             'description': u'每个班都有很多大腿，那么哪个是你最喜欢的呢？！',
             'status': 'already',
             'fillin': 6543,
             'views': 41234,
             'status_display': {
                 'colorclass': 'success',
                 'icon': 'fa-check',
                 'name': u'已发布'
             }
             }
    return sorted([item1, item2], key=lambda x: x['views'] + x['fillin'] * 100, reverse=True)

def get_trash_applications():
    item1 = {'name': u'卧槽被删除了',
             'subscribe_time': '2016.10.06',
             'status': 'trash',
             'id': 2333,
             'description': u'傻了吧',
             'status_display': {
                 'colorclass': 'danger',
                 'icon': 'fa-trash',
                 'name': u'已删除'
             }
    }
    return [item1]


def get_all_applications():
    pending = get_pending_applications()
    already = get_already_applications()
    trash = get_trash_applications()
    pending += already
    pending += trash
    pending += pending
    return pending

def get_official_accounts_with_unprocessed_messages():
    item1 = {'name': u'旗鼓相当的对手',
             'message': u'快看公告！'
             }
    item2 = {'name': u'你的寝室室友',
             'message': u'有人说你妈炸了O^O'
             }
    return [item1, item2]


def get_announcement():
    return u'你妈炸了！！'








def get_applications():
    item1 = {'name': 'u计四五微信平台',
             'description': '计45班的班级微信公众号平台。',
             'status': 'pending',
             'operator_admin_name': '',
             'id': 3
             }
    item2 = {'name': 'u通过示范',
             'description': '一个申请通过的微信公众号平台。',
             'status': 'approved',
             'operator_admin_name': 'admin1',
             'id': 2
             }
    item3 = {'name': 'u尚未提交示范',
             'description': '一个这边还没有提交上去的申请',
             'status': 'not_submitted',
             'operator_admin_name': '',
             'id': 1
             }
    item4 = {'name': '拒绝示范',
             'description': '一个申请被拒的微信公众号平台。',
             'status': 'rejected',
             'operator_admin_name': 'admin3',
             'id': 4
             }
    return [item1, item2, item3, item4]


def get_official_accounts():
    item1 = {'name': u'中老年生活',
             'subscribers': 128984,
             'description': '让你的中老年生活充满精彩。'
             }
    item2 = {'name': u'每日谣言',
             'subscribers': 7276,
             'description': '绝不说假话。'
             }
    return sorted([item1, item2], key=itemgetter('subscribers'), reverse=True)

