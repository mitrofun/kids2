#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from dictionaries.category.views import CategoriesListView, CategoriesCreateView, CategoriesDetailView
from dictionaries.category.views import CategoriesUpdateView, CategoriesDeleteView

urlpatterns = [
    url(r'^$', CategoriesListView.as_view(), name='categories-list'),
    url(r'^add/$', CategoriesCreateView.as_view(), name='categories-add'),
    url(r'^(?P<category>[-\w]+)/$', CategoriesDetailView.as_view(), name='categories-detail'),
    url(r'^(?P<category>[-\w]+)/edit/$', CategoriesUpdateView.as_view(), name='categories-edit'),
    url(r'^(?P<category>[-\w]+)/delete/$', CategoriesDeleteView.as_view(), name='categories-delete'),
    url(r'^(?P<category>[-\w]+)/types/', include('dictionaries.type.urls')),

]
