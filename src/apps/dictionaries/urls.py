#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include


urlpatterns = [
    url(r'', include('dictionaries.category.urls')),
    #  ^(?P<category>[-\w]+)/

    # url(r'^(?P<category>[-\w]+)/types/(?P<dictionary_type>[-\w]+)/items/$',
    #     DictionariesView.as_view(),
    #     name='dictionaries'
    #     ),
    # url(r'^(?P<category>[-\w]+)', name='categories'),
]
