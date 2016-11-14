#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include


urlpatterns = [
    url(r'^v1.0/', include('src.api.v1.urls')),
]