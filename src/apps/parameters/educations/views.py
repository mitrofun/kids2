from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.forms import HiddenInput
from django.views.generic.base import ContextMixin, View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from parameters.models import StudentHistory
from children.models import Child
from parameters.educations.forms import EducationHistoryForm
from datetime import timedelta

template = 'parameters/educations'


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
    template_name = '{}/{}.html'.format(template, 'list')

    def get_queryset(self):
        return StudentHistory.objects.filter(child_id=self.kwargs['child_id'])


class EducationAddView(EducationDetailBaseView, CreateView):
    template_name = '{}/{}.html'.format(template, 'edit')
    fields = '__all__'

    def get_form_class(self):
        return EducationHistoryForm

    def get_form(self, *args, **kwargs):
        form = super(EducationAddView, self).get_form(*args, **kwargs)
        if 'child_id' in self.kwargs:
            form.fields['child'].initial = Child.objects.get(pk=self.kwargs['child_id'])
            form.fields['child'].widget = HiddenInput()
        return form

    def form_valid(self, form):

        one_day = timedelta(days=1)
        next_history = None
        open_history_list = StudentHistory.objects.filter(child=self.kwargs['child_id']).filter(last_date=None)

        if 'child_id' in self.kwargs:
            all_history = StudentHistory.objects.filter(child=self.kwargs['child_id']). \
                order_by('first_date')
            next_history_list = StudentHistory.objects. \
                filter(child=self.kwargs['child_id']). \
                filter(first_date__gt=form.cleaned_data['first_date']).order_by('first_date')
        else:
            all_history = StudentHistory.objects.filter(child=self.kwargs['child_id']). \
                order_by('first_date')
            next_history_list = StudentHistory.objects. \
                filter(child=self.kwargs['child_id']). \
                filter(first_date__gt=form.cleaned_data['first_date']).order_by('first_date')

        if len(all_history):
            for history in all_history:
                if form.cleaned_data['first_date'] <= history.first_date:
                    text_error = 'Ранее сужествует история, установите более раннюю дату'
                    form.errors['first_date'] = [text_error]
                    return self.form_invalid(form)

        if len(next_history_list):
            next_history = next_history_list[0]

        if len(open_history_list):
            for open_history in open_history_list:
                if open_history.first_date <= form.cleaned_data['first_date'] - one_day:
                    open_history.last_date = form.cleaned_data['first_date'] - one_day
                    open_history.save()

        if form.cleaned_data['group'] and form.cleaned_data['grade']:
            text_error = 'Не возможно обновреммено группа и класс.Выберете что-то одно'
            form.errors['group'] = [text_error]
            form.errors['grade'] = [text_error]
            return self.form_invalid(form)

        if form.cleaned_data['last_date']:
            if form.cleaned_data['last_date'] < form.cleaned_data['first_date']:
                text_error = 'Конечная дата не может быть меньше начальной'
                form.errors['last_date'] = [text_error]
                return self.form_invalid(form)

            if next_history:
                if form.cleaned_data['last_date'] > next_history.first_date - one_day:
                    text_error = 'Позже уже есть история.' \
                                 'Конечная дата не может быть больше {}'.format(next_history.first_date - one_day)
                    form.errors['last_date'] = [text_error]
                    return self.form_invalid(form)

        if form.cleaned_data['last_date'] is None and next_history:
            text_error = 'Позже уже есть история.' \
                         'Данная история должна быть закрыта ' \
                         'до {} включительно'.format(next_history.first_date - one_day)
            form.errors['last_date'] = [text_error]
            return self.form_invalid(form)

        return super(EducationAddView, self).form_valid(form)


class EducationDetailView(EducationDetailBaseView, DetailView):
    template_name = '{}/{}.html'.format(template, 'detail')


class EducationUpdateView(EducationDetailBaseView, UpdateView):
    template_name = '{}/{}.html'.format(template, 'edit')
    fields = '__all__'

    def get_form_class(self):
        return EducationHistoryForm

    def get_form(self, *args, **kwargs):
        form = super(EducationUpdateView, self).get_form(*args, **kwargs)
        if 'child_id' in self.kwargs:
            form.fields['child'].initial = Child.objects.get(pk=self.kwargs['child_id'])
            form.fields['child'].widget = HiddenInput()
        return form

    def form_valid(self, form):

        one_day = timedelta(days=1)
        next_history = None
        open_history_list = StudentHistory.objects.filter(child=self.kwargs['child_id']).filter(last_date=None)

        if 'child_id' in self.kwargs:
            all_history = StudentHistory.objects.filter(child=self.kwargs['child_id']).\
                exclude(pk=self.kwargs['education_id']).order_by('first_date')
            next_history_list = StudentHistory.objects. \
                filter(child=self.kwargs['child_id']). \
                exclude(pk=self.kwargs['education_id']). \
                filter(first_date__gt=form.cleaned_data['first_date']).order_by('first_date')
        else:
            all_history = StudentHistory.objects.filter(child=self.kwargs['child_id']). \
                order_by('first_date')
            next_history_list = StudentHistory.objects. \
                filter(child=self.kwargs['child_id']). \
                filter(first_date__gt=form.cleaned_data['first_date']).order_by('first_date')

        if len(all_history):
            for history in all_history:
                if form.cleaned_data['first_date'] <= history.first_date:
                    text_error = 'Ранее сужествует история, установите более раннюю дату'
                    form.errors['first_date'] = [text_error]
                    return self.form_invalid(form)

        if len(next_history_list):
            next_history = next_history_list[0]

        if len(open_history_list):
            for open_history in open_history_list:
                if open_history.first_date <= form.cleaned_data['first_date'] - one_day:
                    open_history.last_date = form.cleaned_data['first_date'] - one_day
                    open_history.save()

        if form.cleaned_data['group'] and form.cleaned_data['grade']:
            text_error = 'Не возможно обновреммено группа и класс.Выберете что-то одно'
            form.errors['group'] = [text_error]
            form.errors['grade'] = [text_error]
            return self.form_invalid(form)

        if form.cleaned_data['last_date']:
            if form.cleaned_data['last_date'] < form.cleaned_data['first_date']:
                text_error = 'Конечная дата не может быть меньше начальной'
                form.errors['last_date'] = [text_error]
                return self.form_invalid(form)

            if next_history:
                if form.cleaned_data['last_date'] > next_history.first_date - one_day:
                    text_error = 'Позже уже есть история.' \
                                 'Конечная дата не может быть больше {}'.format(next_history.first_date - one_day)
                    form.errors['last_date'] = [text_error]
                    return self.form_invalid(form)

        if form.cleaned_data['last_date'] is None and next_history:
            text_error = 'Позже уже есть история.' \
                         'Данная история должна быть закрыта ' \
                         'до {} включительно'.format(next_history.first_date - one_day)
            form.errors['last_date'] = [text_error]
            return self.form_invalid(form)

        return super(EducationUpdateView, self).form_valid(form)


class EducationDeleteView(EducationDetailBaseView, DeleteView):

    def get_success_url(self):
        return reverse_lazy('educations:list', kwargs={'child_id': self.kwargs['child_id']})
