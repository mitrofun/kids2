#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.items.views import DicItemsListView, DicItemsCreateView


urlpatterns = [
    url(r'^$', DicItemsListView.as_view(), name='items-list'),
    url(r'^add/$', DicItemsCreateView.as_view(), name='items-add'),
    # url(r'^(?P<dictionary_type>[-\w]+)/$', DicTypesDetailView.as_view(), name='types-detail'),
    # url(r'^(?P<dictionary_type>[-\w]+)/edit/$', DicTypesUpdateView.as_view(), name='types-edit'),
    # url(r'^(?P<dictionary_type>[-\w]+)/delete/$', DicTypesDeleteView.as_view(), name='types-delete'),
]
