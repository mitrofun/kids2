#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from dictionaries.models import HealthStates

template = 'dictionaries/elementary/'


class HealthBaseView(LoginRequiredMixin, ContextMixin):
    model = HealthStates
    context_object_name = 'obj'
    pk_url_kwarg = 'health_id'


class HealthListView(HealthBaseView, ListView):
    context_object_name = 'obj_list'
    template_name = template + 'list.html'

    def get_queryset(self):
        return HealthStates.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HealthListView, self).get_context_data(**kwargs)
        context['add_obj'] = reverse_lazy('health:add')
        return context


class HealthCreateView(HealthBaseView, CreateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(HealthCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER', reverse_lazy('health:list'))
        return context


class HealthDetailView(HealthBaseView, DetailView):
    template_name = template + 'detail.html'


class HealthUpdateView(HealthBaseView, UpdateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(HealthUpdateView, self).get_context_data(**kwargs)
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('health:detail',
                                               kwargs={'health_id': self.object.id}))
        return context


class HealthDeleteView(HealthBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('health:list')
