#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from src.api.v1.children.serialize import children_list

urlpatterns = [
    url(r'^children/$', children_list, name='children'),
]