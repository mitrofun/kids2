from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import ContextMixin, View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from parameters.models import StudentHistory
from children.models import Child


class EducationBaseView(LoginRequiredMixin, ContextMixin, View):
    model = StudentHistory
    context_object_name = 'education_list'
    pk_url_kwarg = 'education_id'

    def get_context_data(self, **kwargs):
        context = super(EducationBaseView, self).get_context_data(**kwargs)
        if 'child_id' in self.kwargs:
            context['child'] = Child.objects.get(id=self.kwargs['child_id'])
        return context


class EducationDetailBaseView(EducationBaseView):
    model = StudentHistory
    context_object_name = 'education'


class EducationListView(EducationBaseView, ListView):
    template_name = 'parameters/educations/education_list.html'

    def get_queryset(self):
        return StudentHistory.objects.filter(child_id=self.kwargs['child_id'])


class EducationAddView(EducationDetailBaseView, CreateView):
    template_name = 'parameters/educations/education_edit.html'
    fields = '__all__'


class EducationDetailView(EducationDetailBaseView, DetailView):
    template_name = 'parameters/educations/education_detail.html'


class EducationUpdateView(EducationDetailBaseView, UpdateView):
    template_name = 'parameters/educations/education_edit.html'
    fields = '__all__'


class EducationDeleteView(EducationDetailBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('educations:list')
