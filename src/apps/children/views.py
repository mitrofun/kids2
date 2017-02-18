from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from children.models import Child
from children.forms import ChildForm
from history.models import Param


class ChildrenBaseView(LoginRequiredMixin, ContextMixin):
    model = Child
    context_object_name = 'children'
    pk_url_kwarg = 'child_id'


class ChildBaseView(ChildrenBaseView):
    context_object_name = 'child'


class ChildrenTemplateView(ChildrenBaseView, TemplateView):
    template_name = 'children/children_list.html'


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

    def get_initial_queryset(self):
        return Child.objects.all()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)

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
                 'age': item.get_age()
                 }
            )
        return json_data
