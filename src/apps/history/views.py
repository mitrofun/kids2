from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin, View
from django.views.generic import CreateView
from history.models import ParamHistory, Param
from children.models import Child


class HistoryBaseView(LoginRequiredMixin, ContextMixin, View):
    model = ParamHistory
    context_object_name = 'history'

    def get_context_data(self, **kwargs):
        context = super(HistoryBaseView, self).get_context_data(**kwargs)
        if 'child_id' in self.kwargs:
            context['child'] = Child.objects.get(pk=self.kwargs['child_id'])
            context['param'] = Param.objects.get(slug=self.kwargs['param'])
        return context


class HistoryAddView(HistoryBaseView, CreateView):
    template_name = 'history/edit.html'
    fields = '__all__'
