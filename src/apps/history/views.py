from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin, View
from django.views.generic import CreateView, UpdateView, DeleteView
from history.models import ParamHistory, Param
from children.models import Child
from history.forms import HistoryForm
from django.forms import HiddenInput
from history.helper import PARAM_ACCORDANCE
from datetime import timedelta
from django.core.urlresolvers import reverse_lazy, reverse


class HistoryBaseView(LoginRequiredMixin, ContextMixin, View):
    model = ParamHistory
    context_object_name = 'history'

    def get_context_data(self, **kwargs):
        context = super(HistoryBaseView, self).get_context_data(**kwargs)
        if 'child_id' in self.kwargs:
            context['child'] = Child.objects.get(pk=self.kwargs['child_id'])
            context['param'] = Param.objects.get(slug=self.kwargs['param'])
            context['back_url'] = \
                self.request.META.get('HTTP_REFERER', reverse_lazy('children:detail',
                                                                   kwargs={'child_id': self.kwargs['child_id']}))
        if 'history_id' in self.kwargs:
            context['history'] = ParamHistory.objects.get(pk=self.kwargs['history_id'])
        return context

    def get_success_url(self):
        return reverse_lazy('children:detail', kwargs={'child_id': self.kwargs['child_id']})


class HistoryAddView(HistoryBaseView, CreateView):
    template_name = 'history/edit.html'
    fields = '__all__'

    def get_form_class(self):
        return HistoryForm

    def get_form(self, *args, **kwargs):
        visible_fields = ['first_date', 'last_date']
        form = super(HistoryAddView, self).get_form(*args, **kwargs)
        if 'child_id' in self.kwargs:
            form.fields['child'].initial = Child.objects.get(pk=self.kwargs['child_id'])
            form.fields['parameter'].initial = Param.objects.get(slug=self.kwargs['param'])
            for param in PARAM_ACCORDANCE:
                if self.kwargs['param'] == param['name']:
                    visible_fields.extend(param['params'])
            for field in form.fields:
                if field not in visible_fields:
                    form.fields[field].widget = HiddenInput()
        if self.kwargs['param'] == 'education':
            form.fields['institution'].required = True
        return form

    def form_valid(self, form):

        one_day = timedelta(days=1)
        next_history = None
        open_history_list = ParamHistory.objects.filter(child=self.kwargs['child_id']).filter(last_date=None)

        if 'child_id' in self.kwargs:
            all_history = ParamHistory.objects.filter(child=self.kwargs['child_id']). \
                filter(parameter__slug=self.kwargs['param']). \
                order_by('first_date')
            next_history_list = ParamHistory.objects. \
                filter(child=self.kwargs['child_id']). \
                filter(parameter__slug=self.kwargs['param']). \
                filter(first_date__gt=form.cleaned_data['first_date']).order_by('first_date')
        else:
            all_history = ParamHistory.objects.filter(child=self.kwargs['child_id']). \
                filter(parameter__slug=self.kwargs['param']). \
                order_by('first_date')
            next_history_list = ParamHistory.objects. \
                filter(child=self.kwargs['child_id']). \
                filter(parameter__slug=self.kwargs['param']). \
                filter(first_date__gt=form.cleaned_data['first_date']).order_by('first_date')

        if len(all_history):
            for history in all_history:
                if form.cleaned_data['first_date'] <= history.first_date:
                    text_error = 'Ранее сужествует история, установите более позднюю дату'
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

        return super(HistoryAddView, self).form_valid(form)


class HistoryUpdateView(HistoryBaseView, UpdateView):
    template_name = 'history/edit.html'
    form_class = HistoryForm
    pk_url_kwarg = 'history_id'

    def get_form(self, *args, **kwargs):
        visible_fields = ['first_date', 'last_date']
        form = super(HistoryUpdateView, self).get_form(*args, **kwargs)
        if 'child_id' in self.kwargs:
            form.fields['child'].initial = Child.objects.get(pk=self.kwargs['child_id'])
            form.fields['parameter'].initial = Param.objects.get(slug=self.kwargs['param'])
            for param in PARAM_ACCORDANCE:
                if self.kwargs['param'] == param['name']:
                    visible_fields.extend(param['params'])
            for field in form.fields:
                if field not in visible_fields:
                    form.fields[field].widget = HiddenInput()
                    form.fields[field].disabled = True
        if self.kwargs['param'] == 'education':
            form.fields['institution'].required = True
        return form

    def form_valid(self, form):

        one_day = timedelta(days=1)
        next_history = None
        open_history_list = ParamHistory.objects.filter(child=self.kwargs['child_id']).filter(last_date=None)

        if 'child_id' in self.kwargs:
            all_history = ParamHistory.objects.filter(child=self.kwargs['child_id']). \
                filter(parameter__slug=self.kwargs['param']). \
                exclude(pk=self.kwargs['history_id']). \
                order_by('first_date')
            next_history_list = ParamHistory.objects. \
                filter(child=self.kwargs['child_id']). \
                filter(parameter__slug=self.kwargs['param']). \
                exclude(pk=self.kwargs['history_id']). \
                filter(first_date__gt=form.cleaned_data['first_date']).order_by('first_date')
        else:
            all_history = ParamHistory.objects.filter(child=self.kwargs['child_id']). \
                filter(parameter__slug=self.kwargs['param']). \
                order_by('first_date')
            next_history_list = ParamHistory.objects. \
                filter(child=self.kwargs['child_id']). \
                filter(parameter__slug=self.kwargs['param']). \
                filter(first_date__gt=form.cleaned_data['first_date']).order_by('first_date')

        if len(all_history):
            for history in all_history:
                if form.cleaned_data['first_date'] <= history.first_date:
                    text_error = 'Ранее сужествует история, установите более позднюю дату'
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

        return super(HistoryUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('children:detail', kwargs={'child_id': self.kwargs['child_id']})


class HistoryDeleteView(HistoryBaseView, DeleteView):
    pk_url_kwarg = 'history_id'

    def get_success_url(self):
        return reverse_lazy('children:detail', kwargs={'child_id': self.kwargs['child_id']})
