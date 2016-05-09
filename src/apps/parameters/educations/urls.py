#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from parameters.educations.views import EducationListView, EducationAddView, EducationDetailView
from parameters.educations.views import EducationUpdateView, EducationDeleteView


urlpatterns = [
    url(r'^$', EducationListView.as_view(), name='list'),
    url(r'^add/$', EducationAddView.as_view(), name='add'),
    url(r'^(?P<education_id>[0-9]+)/$', EducationDetailView.as_view(), name='detail'),
    url(r'^(?P<education_id>[0-9]+)/edit/$', EducationUpdateView.as_view(), name='edit'),
    url(r'^(?P<education_id>[0-9]+)/delete/$', EducationDeleteView.as_view(), name='delete'),
]
