#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.category.views import CategoriesListView

urlpatterns = [
    url(r'^$', CategoriesListView.as_view(), name='categories-list'),

    # url(r'^(?P<category>[-\w]+)/types/(?P<dictionary_type>[-\w]+)/items/$',
    #     DictionariesView.as_view(),
    #     name='dictionaries'
    #     ),

]
