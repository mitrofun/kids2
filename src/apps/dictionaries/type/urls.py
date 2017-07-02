# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from dictionaries.type.views import DicTypesListView, DicTypesCreateView, DicTypesDetailView
from dictionaries.type.views import DicTypesUpdateView, DicTypesDeleteView


urlpatterns = [
    url(r'^$', DicTypesListView.as_view(), name='types-list'),
    url(r'^add/$', DicTypesCreateView.as_view(), name='types-add'),
    url(
        r'^(?P<dictionary_type>[-\w]+)/$',
        DicTypesDetailView.as_view(),
        name='types-detail'
    ),
    url(
        r'^(?P<dictionary_type>[-\w]+)/edit/$',
        DicTypesUpdateView.as_view(),
        name='types-edit'
    ),
    url(
        r'^(?P<dictionary_type>[-\w]+)/delete/$',
        DicTypesDeleteView.as_view(),
        name='types-delete'
    ),
    url(
        r'^(?P<dictionary_type>[-\w]+)/items/',
        include('dictionaries.items.urls')),
]
