# -*- coding: utf-8 -*-
from operator import itemgetter


def get_pending_applications():
    item1 = {'name': '诚招女友 欢迎报名',
             'manager_name': '2016.10.01',
             'description': '找个女朋友陪我过十一QAQ'
             }
    item2 = {'name': '名字一定要长名字一定要长名字一定要长',
             'manager_name': '2016.10.04',
             'description': '你一定没见过这么标准的十五个字\n你一定没见过这么标准的十五个字\n你一定没见过这么标准的十五个字\n'
                            '你一定没见过这么标准的十五个字\n你一定没见过这么标准的十五个字\n你一定没见过这么标准的十五个字'
             }
    item3 = {'name': '源：厉害了我的哥',
             'manager_name': '2016.10.05',
             'description': '半藏：当然了我的弟'
             }
    return [item1, item2, item3]


def get_applications():
    item1 = {'name': '计四五微信平台',
             'description': '计45班的班级微信公众号平台。',
             'status': 'pending',
             'operator_admin_name': '',
             'id': 3
             }
    item2 = {'name': '通过示范',
             'description': '一个申请通过的微信公众号平台。',
             'status': 'approved',
             'operator_admin_name': 'admin1',
             'id': 2
             }
    item3 = {'name': '尚未提交示范',
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
    item1 = {'name': '中老年生活',
             'subscribers': 128984,
             'description': '让你的中老年生活充满精彩。'
             }
    item2 = {'name': '每日谣言',
             'subscribers': 7276,
             'description': '绝不说假话。'
             }
    return sorted([item1, item2], key=itemgetter('subscribers'), reverse=True)


def get_activities():
    item1 = {'subscribe_time': '2016.10.04',
             'activity_name': '眼动实验被试者招募',
             'activity_id': 1234,
             'description': '计算机系人工智能研究所搜索引擎相关实验，报酬优厚',
             'fillin': 11232,
             'views': 343241
             }
    item2 = {'subscribe_time': '2016.06.02',
             'activity_name': '票选你最喜欢的大腿活动',
             'activity_id': 5678,
             'description': '每个班都有很多大腿，那么哪个是你最喜欢的呢？！快来投票吧',
             'fillin': 6543,
             'views': 41234
             }
    return sorted([item1, item2], key=lambda x: x['views'] + x['fillin'] * 100, reverse=True)


def get_official_accounts_with_unprocessed_messages():
    item1 = {'name': '旗鼓相当的对手',
             'message': '快看公告！'
             }
    item2 = {'name': '你的寝室室友',
             'message': '有人说你妈炸了O^O'
             }
    return [item1, item2]


def get_announcement():
    return '你妈炸了！！'