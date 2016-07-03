#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from dictionaries.education.views import EducationView

urlpatterns = [
    url(r'^$', EducationView.as_view(), name='education'),
    url(r'^institutions/', include('dictionaries.education.institutions.urls', namespace='institutions')),
    # url(r'^groups/', include('dictionaries.education.groups.urls', namespace='groups')),
    # url(r'^grades/', include('dictionaries.education.grades.urls', namespace='grades')),
]