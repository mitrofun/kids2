#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url, include
from children.views import ChildrenTemplateView, ChildrenDetailView, ChildrenUpdateView
from children.views import ChildrenCreateView, ChildrenDeleteView


urlpatterns = [
    url(r'^$', ChildrenTemplateView.as_view(), name='list'),
    url(r'^add/$', ChildrenCreateView.as_view(), name='add'),

    url(r'^(?P<child_id>[0-9]+)/$', ChildrenDetailView.as_view(), name='detail'),
    url(r'^(?P<child_id>[0-9]+)/edit/$', ChildrenUpdateView.as_view(), name='edit'),
    url(r'^(?P<child_id>[0-9]+)/delete/$', ChildrenDeleteView.as_view(), name='delete'),

    url(r'^(?P<child_id>[0-9]+)/params/', include('history.urls')),
]
