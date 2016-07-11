#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.items.views import DicTypesListView


urlpatterns = [
    url(r'^$', DicTypesListView.as_view(), name='items-list'),
    # url(r'^add/$', DicTypesCreateView.as_view(), name='types-add'),
    # url(r'^(?P<dictionary_type>[-\w]+)/$', DicTypesDetailView.as_view(), name='types-detail'),
    # url(r'^(?P<dictionary_type>[-\w]+)/edit/$', DicTypesUpdateView.as_view(), name='types-edit'),
    # url(r'^(?P<dictionary_type>[-\w]+)/delete/$', DicTypesDeleteView.as_view(), name='types-delete'),
]
