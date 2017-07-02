# -*- coding: utf-8 -*-

from django.conf.urls import url

from history.views import HistoryAddView, HistoryUpdateView, HistoryDeleteView


urlpatterns = [
    url(
        r'^(?P<param>[-\w]+)/history/add/$',
        HistoryAddView.as_view(),
        name='history-add'
    ),
    url(
        r'^(?P<param>[-\w]+)/history/(?P<history_id>[0-9]+)/edit/$',
        HistoryUpdateView.as_view(),
        name='history-edit'
    ),
    url(
        r'^(?P<param>[-\w]+)/history/(?P<history_id>[0-9]+)/delete/$',
        HistoryDeleteView.as_view(),
        name='history-delete'
    )
]
