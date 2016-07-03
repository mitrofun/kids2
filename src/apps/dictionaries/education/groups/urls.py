#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.education.groups.views import GroupListView, GroupCreateView, GroupDetailView
from dictionaries.education.groups.views import GroupUpdateView, GroupDeleteView

urlpatterns = [
    url(r'^$', GroupListView.as_view(), name='list'),
    url(r'^add/$', GroupCreateView.as_view(), name='add'),
    url(r'^(?P<group_id>[0-9]+)/$', GroupDetailView.as_view(), name='detail'),
    url(r'^(?P<group_id>[0-9]+)/edit/$', GroupUpdateView.as_view(), name='edit'),
    url(r'^(?P<group_id>[0-9]+)/delete/$', GroupDeleteView.as_view(), name='delete'),
]
