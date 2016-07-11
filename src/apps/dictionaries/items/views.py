#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from dictionaries.models import Dictionary, Category, DictionariesType
from django.core.urlresolvers import reverse_lazy

template = 'dictionaries/items/'


class DictionaryDaseView(LoginRequiredMixin, ContextMixin):
    model = Dictionary
    context_object_name = 'item'
    slug_url_kwarg = 'dictionary_id'


class DicTypesListView(DictionaryDaseView, ListView):
    context_object_name = 'items'
    template_name = template + 'list.html'

    def get_queryset(self):
        return Dictionary.objects.filter(type__slug=self.kwargs['dictionary_type'])

    def get_context_data(self, **kwargs):
        context = super(DicTypesListView, self).get_context_data(**kwargs)
        context['add_types'] = reverse_lazy('dictionaries:types-add', kwargs={'category': self.kwargs['category']})
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['type'] = DictionariesType.objects.get(slug=self.kwargs['dictionary_type'])
        return context
