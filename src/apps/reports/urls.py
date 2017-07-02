#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from reports.views import status_view, reports_view, reports_file


urlpatterns = [
    url(r'^$', reports_view, name='index'),
    url(r'^status/$', status_view, name="status"),
    url(r'^get/$', reports_file, name="get"),
]
