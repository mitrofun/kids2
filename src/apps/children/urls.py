#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url
from children.views import ChildrenListView
from django_filters.views import FilterView
from children.filters import ChildrenFilter

urlpatterns = [
    url(r'^$', ChildrenListView.as_view(), name='list'),
    url(r'^filter/$', FilterView.as_view(filterset_class=ChildrenFilter)),

]
