#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from dictionaries.education.institutions.views import InstitutionListView, InstitutionCreateView, InstitutionDetailView
from dictionaries.education.institutions.views import InstitutionUpdateView, InstitutionDeleteView

urlpatterns = [
    url(r'^$', InstitutionListView.as_view(), name='list'),
    url(r'^add/$', InstitutionCreateView.as_view(), name='add'),
    url(r'^(?P<institution_id>[0-9]+)/$', InstitutionDetailView.as_view(), name='detail'),
    url(r'^(?P<institution_id>[0-9]+)/edit/$', InstitutionUpdateView.as_view(), name='edit'),
    url(r'^(?P<institution_id>[0-9]+)/delete/$', InstitutionDeleteView.as_view(), name='delete'),
]
