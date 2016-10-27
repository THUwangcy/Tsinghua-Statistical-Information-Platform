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
             'type': 'recruit',
             'id': 1000,
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
             'type': 'vote',
             'id': 2000,
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
             'type': 'enroll',
             'id': 3000,
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
    return [item1, item2, item3]


def get_already_applications():
    item1 = {'subscribe_time': '2016.10.04',
             'name': u'眼动实验被试者招募',
             'id': 1234,
             'description': u'计算机系人工智能研究所搜索引擎相关实验，报酬优厚',
             'status': 'already',
             'type': 'recruit',
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
             'type': 'recruit',
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
             'type': 'recruit',
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

def get_participants():
    item1 = {
        'id': 1,
        'fillin_time': '2016.10.06',
        'ip': '127.0.0.1',
        'city': u'北京'
    }
    item2 = {
        'id': 2,
        'fillin_time': '2016.10.06',
        'ip': '127.0.0.1',
        'city': u'北京'
    }
    item3 = {
        'id': 3,
        'fillin_time': '2016.10.06',
        'ip': '127.0.0.1',
        'city': u'北京'
    }
    item4 = {
        'id': 4,
        'fillin_time': '2016.10.06',
        'ip': '127.0.0.1',
        'city': u'北京'
    }
    return [item1, item2, item3, item4]

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


def get_questionnaire_byID(act_id):
    result = {}
    if act_id == '1000':
        act_type = 'recruit'
        act_status = 'pending'
        act_title = u'诚招女友 欢迎报名'
        act_description = u'找个女朋友陪我过十一QAQ'
        qst_num = 2

        qst1 = {'qst_type': 'single',
                'qst_title': u'第一道单选题',
                'qst_id': 1, 
                'option_num': 2,
                'option': [u'###第一个选项###', u'###第二个选项###']
                }
        qst2 = {'qst_type': 'single',
                'qst_title': u'第二道单选题',
                'qst_id': 2,
                'option_num': 3,
                'option': [u'###选项 1###', u'###选项 2###', u'###选项 3###']
                }

        questions = [qst1, qst2]

        result = {'act_type': act_type,
                  'act_status': act_status,
                  'act_title': act_title,
                  'act_description': act_description,
                  'qst_num': qst_num,
                  'questions': questions
                  }
    elif act_id == '2000':
        act_type = 'vote'
        act_status = 'pending'
        act_title = u'名字一定要长名字一定要长名字一定要长'
        act_description = u'你一定没见过这么标准的十五个字'
        qst_num = 3

        qst1 = {'qst_type': 'single',
                'qst_title': u'第一道单选题',
                'qst_id': 1, 
                'option_num': 2,
                'option': [u'###第一个选项###', u'###第二个选项###']
                }
        qst2 = {'qst_type': 'single',
                'qst_title': u'第二道单选题',
                'qst_id': 2,
                'option_num': 3,
                'option': [u'###选项 1###', u'###选项 2###', u'###选项 3###']
                }
        qst3 = {'qst_type': 'multi',
                'qst_title': u'第三道多选题',
                'qst_id': 3,
                'option_num': 3,
                'option': [u'###选项一###', u'###选项二###', u'###选项三###']
                }

        questions = [qst1, qst2, qst3]

        result = {'act_type': act_type,
                  'act_status': act_status,
                  'act_title': act_title,
                  'act_description': act_description,
                  'qst_num': qst_num,
                  'questions': questions
                  }
    elif act_id == '3000':
        act_type = 'enroll'
        act_status = 'pending'
        act_title = u'源：厉害了我的哥'
        act_description = u'半藏：当然了我的弟'
        qst_num = 1

        qst1 = {'qst_type': 'single',
                'qst_title': u'源氏说的对不对啊？',
                'qst_id': 1, 
                'option_num': 2,
                'option': [u'###对，太对了###', u'###什么玩意...###']
                }
        qst2 = {'qst_type': 'fillin',
                'qst_title': u'你怎么看？',
                'qst_id': 2, 
                'rows': 1,
                'hint': u'元芳',
                'check': u'文本'
                }

        questions = [qst1, qst2]

        result = {'act_type': act_type,
                  'act_status': act_status,
                  'act_title': act_title,
                  'act_description': act_description,
                  'qst_num': qst_num,
                  'questions': questions
                  }
    else:
        result = {'act_status': 'new'}

    return result


def get_result_of_question(act_id, qst_id, fillin_id):
    result = ''
    if act_id == '1000':
        if int(qst_id) % 2 == 1:
            if fillin_id == '1':
                result = 2
            else:
                result = 1
        else:
            result = 1
    elif act_id == '2000':
        if qst_id == '3':
            if fillin_id == '1':
                result = [1, 2]
            else:
                result = [2, 3]
        else:
            result = 2
    elif act_id == '3000':
        if qst_id == '2':
            if fillin_id == '1':
                result = '对'
            else:
                result = '不对'
        else:
            result = 1

    return result


def get_statistics_of_question(qst_id):
    if int(qst_id) % 3 == 1:
        item1 = {
            'id': 1,
            'content': '第一个选项',
            'count': 1,
            'percentage': 25,
            'total': 4
        }
        item2 = {
            'id': 2,
            'content': '第二个选项',
            'count': 3,
            'percentage': 75,
            'total': 4
        }
        return [item1, item2]
    elif int(qst_id) % 3 == 2:
        item1 = {
            'id': 1,
            'content': '选项 1',
            'count': 1,
            'percentage': 25,
            'total': 4
        }
        item2 = {
            'id': 2,
            'content': '选项 2',
            'count': 2,
            'percentage': 50,
            'total': 4
        }
        item3 = {
            'id': 3,
            'content': '选项 3',
            'count': 1,
            'percentage': 25,
            'total': 4
        }
        return [item1, item2, item3]
    else:
        item1 = {
            'id': 1,
            'content': '填空1',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item2 = {
            'id': 2,
            'content': '这是一个非常长非常长非常长非常长非常长非常长非常长非常长非常长非常长非常长非常长非常长非常长非常长的答案',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item3 = {
            'id': 3,
            'content': '填空3',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item4 = {
            'id': 4,
            'content': '填空4',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item5 = {
            'id': 5,
            'content': '填空5',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item6 = {
            'id': 6,
            'content': '填空6',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item7 = {
            'id': 7,
            'content': '填空7',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item8 = {
            'id': 8,
            'content': '填空8',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item9 = {
            'id': 9,
            'content': '填空9',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item10 = {
            'id': 10,
            'content': '填空10',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
        item11 = {
            'id': 11,
            'content': '填空11',
            'count': 1,
            'percentage': 25,
            'total': 11
        }
    return [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11]



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


def get_activities():
    item1 = {'name': '活动1',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description' : '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item2 = {'name': '活动2',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item3 = {'name': '活动3',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item4 = {'name': '活动4',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item5 = {'name': '活动5',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item6 = {'name': '活动6',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item7 = {'name': '活动7',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item8 = {'name': '活动8',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item9 = {'name': '活动9',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item10 = {'name': '活动10',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item11 = {'name': '活动11',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    item12 = {'name': '活动12',
             'subscribe_time': '2016.10.17',
             'publisher': '王晨阳',
             'description': '这是给管理员看的信息这是给管理员看的信息这是给管理员看的信息'}
    return [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12]


def get_users():
    item1 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item2 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item3 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item4 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item5 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item6 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item7 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item8 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item9 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item10 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item11 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    item12 = {
        'name': '2014011407',
        'identity': 'legalUser',
        'email': 'thuwangcy@gmail.com',
        'telephone_number': '17888802343',
        'real_name': '王晨阳',
    }
    return [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12]
