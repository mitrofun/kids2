#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.secondary.parents.views import ParentsListView, ParentsCreateView, ParentsDetailView
from dictionaries.secondary.parents.views import ParentsUpdateView, ParentsDeleteView

urlpatterns = [
    url(r'^$', ParentsListView.as_view(), name='list'),
    url(r'^add/$', ParentsCreateView.as_view(), name='add'),
    url(r'^(?P<parent_id>[0-9]+)/$', ParentsDetailView.as_view(), name='detail'),
    url(r'^(?P<parent_id>[0-9]+)/edit/$', ParentsUpdateView.as_view(), name='edit'),
    url(r'^(?P<parent_id>[0-9]+)/delete/$', ParentsDeleteView.as_view(), name='delete'),
]
