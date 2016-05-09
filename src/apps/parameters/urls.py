#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<child_id>[0-9]+)/educations/',
        include('parameters.educations.urls', namespace='educations')),
]
