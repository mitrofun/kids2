#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from children.views import ChildrenTemplateView, ChildrenDetailView, ChildrenUpdateView
from children.views import ChildrenCreateView, ChildrenDeleteView, ChildListJson


urlpatterns = [
    url(r'^$', ChildrenTemplateView.as_view(), name='list'),
    url(r'^add/$', ChildrenCreateView.as_view(), name='add'),

    url(r'^(?P<child_id>[0-9]+)/$', ChildrenDetailView.as_view(), name='detail'),
    url(r'^(?P<child_id>[0-9]+)/edit/$', ChildrenUpdateView.as_view(), name='edit'),
    url(r'^(?P<child_id>[0-9]+)/delete/$', ChildrenDeleteView.as_view(), name='delete'),

    url(r'^(?P<child_id>[0-9]+)/params/', include('history.urls')),

    url(r'^data-table/$', login_required(ChildListJson.as_view()), name='child_list_json')
]
