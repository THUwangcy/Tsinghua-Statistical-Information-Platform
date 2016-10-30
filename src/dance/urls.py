"""dance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'test', 'interface.views.test', name='test'),

    #dashboard
    url(r'^legalUser/?$', 'interface.views.legalUser', name='legalUser'),
    url(r'^legalUser/dashboard/?$', 'interface.views.legalUser_dashboard', name='legalUser/dashboard'),

    #applications
    url(r'^legalUser/applications/(\w+)/?$', 'interface.views.legalUser_show_applications', name='legalUser/applications'),
    url(r'^legalUser/applications/(\w+)/list/?$', 'interface.views.legalUser_show_applications_list',
        name='legalUser/applications-list'),

    url(r'^manager/applications/activities/?$', 'interface.views.manager_all_activities',
        name='manager/applications_activities'),
    url(r'^manager/applications/activities/list/?$', 'interface.views.manager_all_activities_list',
        name='manager/applications_activities_list'),

    url(r'^manager/applications/users/?$', 'interface.views.manager_all_users',
        name='manager/applications_users'),
    url(r'^manager/applications/users/list/?$', 'interface.views.manager_all_users_list',
        name='manager/applications_users_list'),

    #design
    url(r'^legalUser/design/(\w+)/?$', 'interface.views.legalUser_show_applications', name='legalUser/design'),
    url(r'^legalUser/design/(\w+)/([0-9]+)/?$', 'interface.views.legalUser_design', name='legalUser/design/id'),
    url(r'^legalUser/design/(\w+)/([0-9]+)/question/?$', 'interface.views.legalUser_design_question',
        name='legalUser/design/question'),

    url(r'^guest/design/(\w+)/?$', 'interface.views.guest_show_applications', name='guest/design'),
    url(r'^guest/design/(\w+)/([0-9]+)/?$', 'interface.views.guest_design', name='guest/design/id'),

    #modal
    url(r'^modal/?$', 'interface.views.show_modal', name='legalUser/modal'),

    #api
    url(r'^api/modify_name/?$', 'api.views.modify_name', name='api/modify_name'),
    url(r'^api/create_new_act/?$', 'api.views.create_new_act', name='api/create_new_act'),
    url(r'^api/create_new_notice/?$', 'api.views.create_new_notice', name='api/create_new_notice'),
    url(r'^api/create_new_qst/?$', 'api.views.create_new_qst', name='api/create_new_qst'),
    url(r'^api/operation_qst/?$', 'api.views.operation_qst', name='api/operation_qst'),
    url(r'^api/remove_act/?$', 'api.views.remove_act', name='api/remove_act'),
    url(r'^api/save_act/?$', 'api.views.save_act', name='api/save_act'),
    url(r'^api/publish_act/?$', 'api.views.publish_act', name='api/publish_act'),
    url(r'^api/modify_qst/?$', 'api.views.modify_qst', name='api/modify_qst'),
    url(r'^api/stop_act/?$', 'api.views.stop_act', name='api/stop_act'),

    url(r'^api/info_change_act/?$', 'api.views.info_change_act', name='api/info_change_act'),
    url(r'^api/login_act/?$', 'api.views.login_act', name='api/login_act'),
    url(r'^api/notice_act/?$', 'api.views.notice_act', name='api/notice_act'),

    url(r'^api/qst_submit/?$', 'api.views.questionnaire_submit', name='api/qst_submit'),

    #userlist
    url(r'^/?$', RedirectView.as_view(url='/login/')),
    url(r'^login/?$', 'interface.views.login_page', name='legalUser/login'),
    url(r'^legalUser/logoff/?$', 'interface.views.log_off', name='legalUser/log_off'),
    url(r'^legalUser/information/?$', 'interface.views.user_information', name='legalUser/information'),
    url(r'^legalUser/information/change/?$', 'interface.views.user_information_change', name='legalUser/information_change'),

    #questionnaire
    url(r'^questionnaire/([0-9]+)/?$', 'interface.views.questionnaire', name='questionnaire'),
    url(r'^questionnaire/(\w+)/([0-9]+)/publish_qst/?$', 'interface.views.questionnaire_publish_question', name='questionnaire/publish_qst'),
    url(r'^fillin/questionnaire/([0-9]+)/([0-9]+)/?$', 'interface.views.fillin_questionnaire', name='fillin/questionnaire'),

    #guest
    url(r'^guest/?$', 'interface.views.guest', name='guest'),
    url(r'^guest/dashboard/?$', 'interface.views.guest_dashboard', name='guest/dashboard'),

    #manager
    url(r'^manager/?$', 'interface.views.manager', name='manager'),
    url(r'^manager/dashboard/?$', 'interface.views.manager_dashboard', name='manager/dashboard'),
    url(r'^manager/notice/?$', 'interface.views.manager_notice', name='manager/notice'),

    #statistics
    url(r'^statistics/?$', 'interface.views.show_statistics_choose', name='statistics'),
    url(r'^statistics/([0-9]+)/?$', 'interface.views.show_statistics', name='statistics/id'),
    url(r'^statistics/([0-9]+)/paticipants', 'interface.views.show_paticipants_list', name='statistics/participants'),
    url(r'^statistics/([0-9]+)/question/?$', 'interface.views.statistics_question', name='statistics/question'),
    url(r'^statistics/([0-9]+)/question/list/(\w+)/([0-9]+)/?$', 'interface.views.statistics_question_list', name='statistics/question/list'),

]
