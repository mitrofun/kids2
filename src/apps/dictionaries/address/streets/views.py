#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from dictionaries.models import Street

template = 'dictionaries/elementary/'


class StreetBaseView(LoginRequiredMixin, ContextMixin):
    model = Street
    context_object_name = 'obj'
    pk_url_kwarg = 'street_id'


class StreetListView(StreetBaseView, ListView):
    context_object_name = 'obj_list'
    template_name = template + 'list.html'

    def get_queryset(self):
        return Street.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StreetListView, self).get_context_data(**kwargs)
        context['add_obj'] = reverse_lazy('streets:add')
        return context


class StreetCreateView(StreetBaseView, CreateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(StreetCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER', reverse_lazy('streets:list'))
        return context


class StreetDetailView(StreetBaseView, DetailView):
    template_name = template + 'detail.html'


class StreetUpdateView(StreetBaseView, UpdateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(StreetUpdateView, self).get_context_data(**kwargs)
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('streets:detail',
                                               kwargs={'street_id': self.object.id}))
        return context


class StreetDeleteView(StreetBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('streets:list')
