#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from dictionaries.secondary.views import SecondaryView

urlpatterns = [
    url(r'^$', SecondaryView.as_view(), name='secondary'),
    url(r'^health/', include('dictionaries.secondary.health.urls', namespace='health')),
    url(r'^parents/', include('dictionaries.secondary.parents.urls', namespace='parents')),
]