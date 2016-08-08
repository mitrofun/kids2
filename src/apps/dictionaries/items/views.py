#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from dictionaries.models import Dictionary, Category, DictionariesType
from django.core.urlresolvers import reverse_lazy

template = 'dictionaries/items/'


class DictionaryBaseView(LoginRequiredMixin, ContextMixin):
    model = Dictionary
    context_object_name = 'dict_item'
    pk_url_kwarg = 'dictionary_id'


class DicItemsListView(DictionaryBaseView, ListView):
    context_object_name = 'items'
    template_name = template + 'list.html'

    def get_queryset(self):
        return Dictionary.objects.filter(type__slug=self.kwargs['dictionary_type'])

    def get_context_data(self, **kwargs):
        context = super(DicItemsListView, self).get_context_data(**kwargs)
        context['add_item'] = reverse_lazy('dictionaries:items-add',
                                           kwargs={
                                               'category': self.kwargs['category'],
                                               'dictionary_type': self.kwargs['dictionary_type']
                                                  }
                                           )
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['type'] = DictionariesType.objects.get(slug=self.kwargs['dictionary_type'])
        return context


class DicItemsCreateView(DictionaryBaseView, CreateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DicItemsCreateView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['type'] = DictionariesType.objects.get(slug=self.kwargs['dictionary_type'])
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('dictionaries:items-list',
                                               kwargs={'category': self.kwargs['category'],
                                                       'dictionary_type': self.kwargs['dictionary_type']
                                                       }
                                               )
                                  )
        return context

    def get_success_url(self):
        return reverse_lazy('dictionaries:items-list',
                            kwargs={'category': self.kwargs['category'],
                                    'dictionary_type': self.kwargs['dictionary_type']
                                    }
                            )


class DicItemsDetailView(DictionaryBaseView, DetailView):
    template_name = template + 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(DicItemsDetailView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['type'] = DictionariesType.objects.get(slug=self.kwargs['dictionary_type'])
        return context


class DicItemsUpdateView(DictionaryBaseView, UpdateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(DicItemsUpdateView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['type'] = DictionariesType.objects.get(slug=self.kwargs['dictionary_type'])
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('dictionaries:items-list',
                                               kwargs={'category': self.kwargs['category'],
                                                       'dictionary_type': self.kwargs['dictionary_type']
                                                       }
                                               )
                                  )
        return context


class DicItemsDeleteView(DictionaryBaseView, DeleteView):
    pass

    def get_success_url(self):
        return reverse_lazy('dictionaries:items-list',
                            kwargs={'category': self.kwargs['category'],
                                    'dictionary_type': self.kwargs['dictionary_type']
                                    }
                            )
