#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from children.models import Child
from dictionaries.models import Dictionary


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        context['children'] = Child.objects.all().count()
        context['institution'] = Dictionary.objects.filter(type__slug="institutions").count()
        context['locality'] = Dictionary.objects.filter(type__slug="locality").count()
        context['street'] = Dictionary.objects.filter(type__slug="streets").count()

        return context
