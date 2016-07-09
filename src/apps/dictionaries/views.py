from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from dictionaries.models import Dictionary

template = 'dictionaries/elementary/'


class DictionariesView(TemplateView):
    template_name = 'dictionaries/dictionaries.html'


class DictionariesBaseView(LoginRequiredMixin, ContextMixin):
    model = Dictionary
    context_object_name = 'obj'
    pk_url_kwarg = 'street_id'


class DictionariesListView(DictionariesBaseView, ListView):
    context_object_name = 'obj_list'
    template_name = template + 'list.html'

    def get_queryset(self):
        return Dictionary.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DictionariesListView, self).get_context_data(**kwargs)
        context['add_obj'] = reverse_lazy('streets:add')
        return context
