#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from dictionaries.models import Institution

template = 'dictionaries/elementary/'


class InstitutionBaseView(LoginRequiredMixin, ContextMixin):
    model = Institution
    context_object_name = 'obj'
    pk_url_kwarg = 'institution_id'


class InstitutionListView(InstitutionBaseView, ListView):
    context_object_name = 'obj_list'
    template_name = template + 'list.html'

    def get_queryset(self):
        return Institution.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InstitutionListView, self).get_context_data(**kwargs)
        context['add_obj'] = reverse_lazy('institutions:add')
        context['institution'] = True
        return context


class InstitutionCreateView(InstitutionBaseView, CreateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(InstitutionCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER', reverse_lazy('institutions:list'))
        return context


class InstitutionDetailView(InstitutionBaseView, DetailView):
    template_name = template + 'detail.html'


class InstitutionUpdateView(InstitutionBaseView, UpdateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(InstitutionUpdateView, self).get_context_data(**kwargs)
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('institutions:detail',
                                               kwargs={'institution_id': self.object.id}))
        return context


class InstitutionDeleteView(InstitutionBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('institutions:list')
