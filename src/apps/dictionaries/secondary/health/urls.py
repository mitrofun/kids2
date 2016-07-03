#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.secondary.health.views import HealthListView, HealthCreateView, HealthDetailView
from dictionaries.secondary.health.views import HealthUpdateView, HealthDeleteView

urlpatterns = [
    url(r'^$', HealthListView.as_view(), name='list'),
    url(r'^add/$', HealthCreateView.as_view(), name='add'),
    url(r'^(?P<health_id>[0-9]+)/$', HealthDetailView.as_view(), name='detail'),
    url(r'^(?P<health_id>[0-9]+)/edit/$', HealthUpdateView.as_view(), name='edit'),
    url(r'^(?P<health_id>[0-9]+)/delete/$', HealthDeleteView.as_view(), name='delete'),
]
