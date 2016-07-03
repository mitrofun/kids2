from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from children.models import Child


class ChildrenBaseView(LoginRequiredMixin, ContextMixin):
    model = Child
    context_object_name = 'children'
    pk_url_kwarg = 'child_id'


class ChildBaseView(ChildrenBaseView):
    context_object_name = 'child'


class ChildrenListView(ChildrenBaseView, ListView):
    template_name = 'children/children_list.html'

    def get_queryset(self):
        return Child.objects.all()


class ChildrenCreateView(ChildBaseView, CreateView):
    template_name = 'children/children_edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ChildrenCreateView, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER', reverse_lazy('children:list'))
        return context


class ChildrenDetailView(ChildBaseView, DetailView):
    template_name = 'children/children_detail.html'


class ChildrenUpdateView(ChildBaseView, UpdateView):
    template_name = 'children/children_edit.html'
    fields = '__all__'

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
