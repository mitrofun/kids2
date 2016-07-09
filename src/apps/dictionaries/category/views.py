#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from dictionaries.models import Category


class CategoriesListView(LoginRequiredMixin, ListView):
    template_name = 'dictionaries/items/list.html'
    context_object_name = 'obj_list'
    model = Category


