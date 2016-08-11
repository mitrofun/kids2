#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from history.views import HistoryAddView


urlpatterns = [
    url(r'^(?P<param>[-\w]+)/history/add/$', HistoryAddView.as_view(), name='history-add')
]
