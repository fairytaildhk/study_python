# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 15:28
# @Author  : huangkaiding
from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)$', views.topic, name='topic'),
]