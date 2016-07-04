#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from dictionaries.models import Locality

template = 'dictionaries/elementary/'


class LocalityBaseView(LoginRequiredMixin, ContextMixin):
    model = Locality
    context_object_name = 'obj'
    pk_url_kwarg = 'locality_id'


class LocalityListView(LocalityBaseView, ListView):
    context_object_name = 'obj_list'
    template_name = template + 'list.html'

    def get_queryset(self):
        return Locality.objects.all()

    def get_context_data(self, **kwargs):
        context = super(LocalityListView, self).get_context_data(**kwargs)
        context['add_obj'] = reverse_lazy('locality:add')
        return context


class LocalityCreateView(LocalityBaseView, CreateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LocalityCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER', reverse_lazy('locality:list'))
        return context


class LocalityDetailView(LocalityBaseView, DetailView):
    template_name = template + 'detail.html'


class LocalityUpdateView(LocalityBaseView, UpdateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LocalityUpdateView, self).get_context_data(**kwargs)
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('locality:detail',
                                               kwargs={'locality_id': self.object.id}))
        return context


class LocalityDeleteView(LocalityBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('locality:list')
