#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.address.streets.views import StreetListView, StreetCreateView, StreetDetailView
from dictionaries.address.streets.views import StreetUpdateView, StreetDeleteView

urlpatterns = [
    url(r'^$', StreetListView.as_view(), name='list'),
    url(r'^add/$', StreetCreateView.as_view(), name='add'),
    url(r'^(?P<street_id>[0-9]+)/$', StreetDetailView.as_view(), name='detail'),
    url(r'^(?P<street_id>[0-9]+)/edit/$', StreetUpdateView.as_view(), name='edit'),
    url(r'^(?P<street_id>[0-9]+)/delete/$', StreetDeleteView.as_view(), name='delete'),
]
