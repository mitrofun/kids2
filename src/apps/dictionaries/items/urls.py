#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.items.views import DicItemsListView, DicItemsCreateView, \
    DicItemsDetailView, DicItemsUpdateView, DicItemsDeleteView


urlpatterns = [
    url(r'^$', DicItemsListView.as_view(), name='items-list'),
    url(r'^add/$', DicItemsCreateView.as_view(), name='items-add'),
    url(r'^(?P<dictionary_id>[0-9]+)/$', DicItemsDetailView.as_view(), name='items-detail'),
    url(r'^(?P<dictionary_id>[0-9]+)/edit/$', DicItemsUpdateView.as_view(), name='items-edit'),
    url(r'^(?P<dictionary_id>[0-9]+)/delete/$', DicItemsDeleteView.as_view(), name='items-delete'),
]
