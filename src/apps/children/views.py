import json
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.views.generic.base import ContextMixin
from django_datatables_view.base_datatable_view import BaseDatatableView

from children.forms import ChildForm
from children.forms import FilterChildrenForm
from children.models import Child
from common.utils import get_param_on_date, get_qs_by_param_name, get_list_names_in_param
from history.models import Param


class ChildrenBaseView(LoginRequiredMixin, ContextMixin):
    model = Child
    context_object_name = 'children'
    pk_url_kwarg = 'child_id'


class ChildBaseView(ChildrenBaseView):
    context_object_name = 'child'


class ChildrenTemplateView(ChildrenBaseView, TemplateView):
    template_name = 'children/children_list.html'

    def get_context_data(self, **kwargs):
        context = super(ChildrenTemplateView, self).get_context_data(**kwargs)
        context['filter_form'] = FilterChildrenForm
        return context


class ChildrenCreateView(ChildBaseView, CreateView):
    template_name = 'children/children_edit.html'
    form_class = ChildForm

    def get_context_data(self, **kwargs):
        context = super(ChildrenCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER', reverse_lazy('children:list'))
        return context


class ChildrenDetailView(ChildBaseView, DetailView):
    template_name = 'children/children_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ChildrenDetailView, self).get_context_data(**kwargs)
        context['params'] = Param.objects.all()
        return context


class ChildrenUpdateView(ChildBaseView, UpdateView):
    template_name = 'children/children_edit.html'
    form_class = ChildForm

    def get_context_data(self, **kwargs):
        context = super(ChildrenUpdateView, self).get_context_data(**kwargs)
        context['back_url'] = \
            self.request.META.get('HTTP_REFERER',
                                  reverse_lazy('children:detail',
                                               kwargs={'children_id': self.object.id}))
        return context


class ChildrenDeleteView(ChildBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('children:list')


class ChildListJson(BaseDatatableView):
    order_columns = ['last_name', 'birthday']

    def __init__(self):
        super(ChildListJson, self).__init__()
        self.date = datetime.now()

    def get_initial_queryset(self):
        return Child.objects.all()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        _filter = self.request.GET.get(u'columns[0][search][value]', None)

        if _filter:
            children_list = []
            filter_params = json.loads(_filter)

            health_states = []
            mode_health_states = 0
            parents_status = []
            mode_parents_status = 0

            if 'date' in filter_params:
                filter_params['date'] = datetime.strptime(filter_params['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
                self.date = filter_params['date']
            if 'institution' in filter_params:
                qs = get_qs_by_param_name(name='institution', qs=qs, **filter_params)
            if 'group' in filter_params:
                qs = get_qs_by_param_name(name='group', qs=qs, **filter_params)
            if 'grade' in filter_params:
                qs = get_qs_by_param_name(name='grade', qs=qs, **filter_params)
            if 'health_states'in filter_params:
                health_states = get_list_names_in_param(filter_params['health_states'], param='health')
                mode_health_states = filter_params['mode_health_states']
                qs = get_qs_by_param_name(name='health_states', qs=qs, **filter_params)
            if 'parents_status' in filter_params:
                parents_status = get_list_names_in_param(filter_params['parents_status'], param='parents')
                mode_parents_status = filter_params['mode_parents_status']
                qs = get_qs_by_param_name(name='parents_status', qs=qs, **filter_params)

            for child in qs:
                children_list.append([
                    child.id,
                    get_param_on_date(child, 'health', 'health_list', filter_params['date']),
                    get_param_on_date(child, 'parents', 'parents_list', filter_params['date']),
                ])

            if health_states and mode_health_states != 0:

                _children_list = children_list.copy()
                children_list.clear()

                if mode_health_states == 2:

                    _condition = ', '.join([states for states in health_states])
                    for _children in _children_list:
                        if _children[1] == _condition:
                            children_list.append(_children)
                else:

                    _condition = [states for states in health_states]
                    for _children in _children_list:

                        if set(_condition) <= set(_children[1].split(', ')):
                            children_list.append(_children)

                qs = qs.filter(pk__in=set([child[0] for child in children_list]))

            if parents_status and mode_parents_status != 0:

                _children_list = children_list.copy()
                children_list.clear()

                if mode_parents_status == 2:

                    _condition = ', '.join([status for status in parents_status])
                    for _children in _children_list:
                        if _children[2] == _condition:
                            children_list.append(_children)
                else:

                    _condition = [status for status in parents_status]
                    for _children in _children_list:

                        if set(_condition) <= set(_children[2].split(', ')):
                            children_list.append(_children)

                qs = qs.filter(pk__in=list(set([child[0] for child in children_list])))

        if search:

            if search.find(' ') != -1:
                filter_last_name = search.split(' ')[0]
                filter_first_name = search.split(' ')[1]
                qs = qs.filter(last_name__istartswith=filter_last_name,
                               first_name__istartswith=filter_first_name)
            else:
                qs = qs.filter(last_name__istartswith=search)

        return qs

    def prepare_results(self, qs):

        json_data = []

        for item in qs:
            json_data.append(
                {'full_name': item.get_full_name(),
                 'link': item.get_absolute_url(),
                 'age': item.get_age(date=self.date)
                 }
            )
        return json_data
