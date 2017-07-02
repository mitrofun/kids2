# -*- coding: utf-8 -*-

from django.conf.urls import url

from reports.views import reports_view, reports_file


urlpatterns = [
    url(r'^$', reports_view, name='index'),
    url(r'^get/$', reports_file, name="get"),
]
