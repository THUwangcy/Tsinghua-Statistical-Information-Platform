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

    #design
    url(r'^legalUser/design/(\w+)/?$', 'interface.views.legalUser_design', name='legalUser/design'),
    url(r'^legalUser/design/(\w+)/question/?$', 'interface.views.legalUser_design_question', name='legalUser/design/question'),

    #userlist
    url(r'^legalUser/login/$', 'interface.views.login_page', name='legalUser/login'),
    url(r'^legalUser/information/$', 'interface.views.user_information', name='legalUser/information'),
    url(r'^legalUser/information/change$', 'interface.views.user_information_change', name='legalUser/information_change'),

    #guest
    url(r'^guest/$', 'interface.views.guest', name='guest'),
    url(r'^guest/dashboard/$', 'interface.views.guest_dashboard', name='guest/dashboard'),
]
