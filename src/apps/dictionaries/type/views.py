#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from dictionaries.models import DictionariesType, Category
from django.core.urlresolvers import reverse_lazy

template = 'dictionaries/type/'


class DicTypesBaseView(LoginRequiredMixin, ContextMixin):
    model = DictionariesType
    context_object_name = 'type'
    slug_url_kwarg = 'dictionary_type'


class DicTypesListView(DicTypesBaseView, ListView):
    context_object_name = 'types'
    template_name = template + 'list.html'

    def get_queryset(self):
        return DictionariesType.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DicTypesListView, self).get_context_data(**kwargs)
        context['add_category'] = reverse_lazy('dictionaries:types-add')
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        return context


class DicTypesCreateView(DicTypesBaseView, CreateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DicTypesCreateView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['back_url'] = self.request.META.get('HTTP_REFERER',
                                                    reverse_lazy('dictionaries:types-list'))
        return context


class DicTypesDetailView(DicTypesBaseView, DetailView):
    template_name = template + 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(DicTypesDetailView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        return context


class DicTypesUpdateView(DicTypesBaseView, UpdateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DicTypesUpdateView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy(
                                      'dictionaries:types-detail',
                                      kwargs={'category': self.object.category.slug,
                                              'dictionary_type': self.object.slug}))
        return context


class DicTypesDeleteView(DicTypesBaseView, DeleteView):
    pass

    def get_success_url(self):
        return reverse_lazy('dictionaries:types-list')
