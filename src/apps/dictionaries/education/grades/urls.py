#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.education.grades.views import GradeListView, GradeCreateView, GradeDetailView
from dictionaries.education.grades.views import GradeUpdateView, GradeDeleteView

urlpatterns = [
    url(r'^$', GradeListView.as_view(), name='list'),
    url(r'^add/$', GradeCreateView.as_view(), name='add'),
    url(r'^(?P<grade_id>[0-9]+)/$', GradeDetailView.as_view(), name='detail'),
    url(r'^(?P<grade_id>[0-9]+)/edit/$', GradeUpdateView.as_view(), name='edit'),
    url(r'^(?P<grade_id>[0-9]+)/delete/$', GradeDeleteView.as_view(), name='delete'),
]
