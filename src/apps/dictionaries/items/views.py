#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from dictionaries.models import Dictionary, Category, DictionariesType
from django.core.urlresolvers import reverse_lazy
from django.forms.widgets import HiddenInput
from dictionaries.views import EDIT_TEMPLATE, get_template

template = 'dictionaries/items/'


class DictionaryBaseView(LoginRequiredMixin, ContextMixin):
    model = Dictionary
    context_object_name = 'dict_item'
    pk_url_kwarg = 'dictionary_id'


class DicItemsListView(DictionaryBaseView, ListView):
    context_object_name = 'items'
    template_name = get_template(template, 'list')

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
    template_name = EDIT_TEMPLATE
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

    def get_form(self, *args, **kwargs):
        form = super(DicItemsCreateView, self).get_form(*args, **kwargs)
        if 'dictionary_type' in self.kwargs:
            form.fields['type'].initial = DictionariesType.objects.get(slug=self.kwargs['dictionary_type'])
            form.fields['type'].widget = HiddenInput()
            if self.kwargs['dictionary_type'] != 'institutions':
                form.fields['institution_type'].widget = HiddenInput()
        return form

    def get_success_url(self):
        return reverse_lazy('dictionaries:items-list',
                            kwargs={'category': self.kwargs['category'],
                                    'dictionary_type': self.kwargs['dictionary_type']
                                    }
                            )


class DicItemsDetailView(DictionaryBaseView, DetailView):
    template_name = get_template(template, 'detail')

    def get_context_data(self, **kwargs):
        context = super(DicItemsDetailView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['type'] = DictionariesType.objects.get(slug=self.kwargs['dictionary_type'])
        return context


class DicItemsUpdateView(DictionaryBaseView, UpdateView):
    template_name = EDIT_TEMPLATE
    fields = '__all__'

    def get_form(self, *args, **kwargs):
        form = super(DicItemsUpdateView, self).get_form(*args, **kwargs)
        if 'dictionary_type' in self.kwargs:
            form.fields['type'].initial = DictionariesType.objects.get(slug=self.kwargs['dictionary_type'])
            form.fields['type'].widget = HiddenInput()
            if self.kwargs['dictionary_type'] != 'institutions':
                form.fields['institution_type'].widget = HiddenInput()
        return form

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
