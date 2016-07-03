#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from dictionaries.models import ParentsStatus

template = 'dictionaries/parents/parent_'


class ParentsBaseView(LoginRequiredMixin, ContextMixin):
    model = ParentsStatus
    context_object_name = 'parent'
    pk_url_kwarg = 'parent_id'


class ParentsListView(ParentsBaseView, ListView):
    context_object_name = 'parents'
    template_name = template + 'list.html'

    def get_queryset(self):
        return ParentsStatus.objects.all()


class ParentsCreateView(ParentsBaseView, CreateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ParentsCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER', reverse_lazy('parents:list'))
        return context


class ParentsDetailView(ParentsBaseView, DetailView):
    template_name = template + 'detail.html'


class ParentsUpdateView(ParentsBaseView, UpdateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ParentsUpdateView, self).get_context_data(**kwargs)
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('parents:detail',
                                               kwargs={'parent_id': self.object.id}))
        return context


class ParentsDeleteView(ParentsBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('parents:list')
