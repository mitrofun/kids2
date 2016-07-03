#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from dictionaries.models import Group

template = 'dictionaries/groups/group_'


class GroupBaseView(LoginRequiredMixin, ContextMixin):
    model = Group
    context_object_name = 'group'
    pk_url_kwarg = 'group_id'


class GroupListView(GroupBaseView, ListView):
    context_object_name = 'groups'
    template_name = template + 'list.html'

    def get_queryset(self):
        return Group.objects.all()


class GroupCreateView(GroupBaseView, CreateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(GroupCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER', reverse_lazy('groups:list'))
        return context


class GroupDetailView(GroupBaseView, DetailView):
    template_name = template + 'detail.html'


class GroupUpdateView(GroupBaseView, UpdateView):
    template_name = template + 'edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('groups:detail',
                                               kwargs={'group_id': self.object.id}))
        return context


class GroupDeleteView(GroupBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('groups:list')
