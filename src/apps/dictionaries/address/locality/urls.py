#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.address.locality.views import LocalityListView, LocalityCreateView, LocalityDetailView
from dictionaries.address.locality.views import LocalityUpdateView, LocalityDeleteView

urlpatterns = [
    url(r'^$', LocalityListView.as_view(), name='list'),
    url(r'^add/$', LocalityCreateView.as_view(), name='add'),
    url(r'^(?P<locality_id>[0-9]+)/$', LocalityDetailView.as_view(), name='detail'),
    url(r'^(?P<locality_id>[0-9]+)/edit/$', LocalityUpdateView.as_view(), name='edit'),
    url(r'^(?P<locality_id>[0-9]+)/delete/$', LocalityDeleteView.as_view(), name='delete'),
]
