#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url
from children.views import ChildrenListView, ChildrenDetailView, ChildrenUpdateView
from children.views import ChildrenCreateView, ChildrenDeleteView
from django_filters.views import FilterView
from children.filters import ChildrenFilter

urlpatterns = [
    url(r'^$', ChildrenListView.as_view(), name='list'),
    url(r'^add/$', ChildrenCreateView.as_view(), name='add'),

    url(r'^(?P<child_id>[0-9]+)/$', ChildrenDetailView.as_view(), name='detail'),
    url(r'^(?P<child_id>[0-9]+)/edit/$', ChildrenUpdateView.as_view(), name='edit'),
    url(r'^(?P<child_id>[0-9]+)/delete/$', ChildrenDeleteView.as_view(), name='delete'),

    url(r'^filter/$', FilterView.as_view(filterset_class=ChildrenFilter), name='filter'),

]
