# -*- coding: utf-8 -*-


from django.conf.urls import url
from accounts.views import user_login as login, user_logout as logout


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

]
