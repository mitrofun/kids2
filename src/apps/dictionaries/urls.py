# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from dictionaries.views import DictionariesView

urlpatterns = [
    url(r'^$', DictionariesView.as_view(), name='main'),
    url(r'^categories/', include('dictionaries.category.urls')),
]
