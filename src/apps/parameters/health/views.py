from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.forms import HiddenInput
from django.views.generic.base import ContextMixin, View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from parameters.models import HealthHistory
from children.models import Child
from parameters.health.forms import HealthHistoryForm
from datetime import timedelta

template = 'parameters/health'


class HealthBaseView(LoginRequiredMixin, ContextMixin, View):
    model = HealthHistory
    context_object_name = 'health_list'
    pk_url_kwarg = 'health_id'

    def get_context_data(self, **kwargs):
        context = super(HealthBaseView, self).get_context_data(**kwargs)
        if 'child_id' in self.kwargs:
            context['child'] = Child.objects.get(id=self.kwargs['child_id'])
        return context


class HealthDetailBaseView(HealthBaseView):
    model = HealthHistory
    context_object_name = 'health'


class HealthListView(HealthBaseView, ListView):
    template_name = '{}/{}.html'.format(template, 'list')

    def get_queryset(self):
        return HealthHistory.objects.filter(child_id=self.kwargs['child_id'])

