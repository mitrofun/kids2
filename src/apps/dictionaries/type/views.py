#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.views.generic import ListView
from dictionaries.models import DictionariesType
from django.core.urlresolvers import reverse_lazy

template = 'dictionaries/type/'


class DicTypesBaseView(LoginRequiredMixin, ContextMixin):
    model = DictionariesType
    context_object_name = 'obj'
    slug_url_kwarg = 'dictionary_type'


class DicTypesListView(DicTypesBaseView, ListView):
    context_object_name = 'obj_list'
    template_name = template + 'list.html'

    def get_queryset(self):
        return DictionariesType.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DicTypesListView, self).get_context_data(**kwargs)
        context['add_obj'] = reverse_lazy('dictionaries:categories-add')
        context['category'] = self.kwargs['category']
        return context

