#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from dictionaries.models import Grade

template = 'dictionaries/elementary/'


class GradeBaseView(LoginRequiredMixin, ContextMixin):
    model = Grade
    context_object_name = 'obj'
    pk_url_kwarg = 'grade_id'


class GradeListView(GradeBaseView, ListView):
    context_object_name = 'obj_list'
    template_name = template + 'list.html'

    def get_queryset(self):
        return Grade.objects.all()

    def get_context_data(self, **kwargs):
        context = super(GradeListView, self).get_context_data(**kwargs)
        context['add_obj'] = reverse_lazy('grades:add')
        return context


class GradeCreateView(GradeBaseView, CreateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(GradeCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER', reverse_lazy('grades:list'))
        return context


class GradeDetailView(GradeBaseView, DetailView):
    template_name = template + 'detail.html'


class GradeUpdateView(GradeBaseView, UpdateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(GradeUpdateView, self).get_context_data(**kwargs)
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('grades:detail',
                                               kwargs={'grade_id': self.object.id}))
        return context


class GradeDeleteView(GradeBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('grades:list')
