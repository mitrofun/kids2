#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.type.views import DicTypesListView


urlpatterns = [
    url(r'^$', DicTypesListView.as_view(), name='types-list'),
]