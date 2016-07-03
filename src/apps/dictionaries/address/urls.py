#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from dictionaries.address.views import AddressView

urlpatterns = [
    url(r'^$', AddressView.as_view(), name='address'),
    url(r'^locality/', include('dictionaries.address.locality.urls', namespace='locality')),
    url(r'^streets/', include('dictionaries.address.streets.urls', namespace='streets')),
]