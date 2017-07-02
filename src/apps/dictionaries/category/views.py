# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from dictionaries.models import Category
from django.core.urlresolvers import reverse_lazy
from dictionaries.views import EDIT_TEMPLATE, get_template

template = 'dictionaries/category/'


class CategoriesBaseView(LoginRequiredMixin, ContextMixin):
    model = Category
    context_object_name = 'category'
    slug_url_kwarg = 'category'


class CategoriesListView(CategoriesBaseView, ListView):
    context_object_name = 'categories'
    template_name = get_template(template, 'list')

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoriesListView, self).get_context_data(**kwargs)
        context['add_category'] = reverse_lazy('dictionaries:categories-add')
        return context


class CategoriesCreateView(CategoriesBaseView, CreateView):
    template_name = EDIT_TEMPLATE
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CategoriesCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get(
            'HTTP_REFERER', reverse_lazy('dictionaries:categories-list'))
        return context


class CategoriesDetailView(CategoriesBaseView, DetailView):
    template_name = get_template(template, 'detail')


class CategoriesUpdateView(CategoriesBaseView, UpdateView):
    template_name = EDIT_TEMPLATE
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CategoriesUpdateView, self).get_context_data(**kwargs)
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('dictionaries:categories-detail',
                                               kwargs={'category': self.object.slug}))
        return context


class CategoriesDeleteView(CategoriesBaseView, DeleteView):
    pass

    def get_success_url(self):
        return reverse_lazy('dictionaries:categories-list')
