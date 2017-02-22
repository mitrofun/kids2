#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, date
import calendar
from django import forms

from dictionaries.models import Dictionary


def get_last_date():
    current_date = datetime.now()
    last_date = (calendar.monthrange(current_date.year, current_date.month))[1]
    _date = date(current_date.year, current_date.month, last_date)
    return _date


class ReportsForm(forms.Form):

    REPORT_CHOICES = (
        (1, 'Список'),
        (2, 'Свод')
    )

    MODE_CHOICES = [(0, 'С любым статусом из списка'),
                    (1, 'Такие статусы входят в условие'),
                    (2, 'Только все эти статусы')]

    report_date = forms.DateField(label='Дата', initial=get_last_date())

    report_type = forms.ChoiceField(label='Тип отчета', choices=REPORT_CHOICES)

    institution = forms.ModelChoiceField(Dictionary.objects.filter(type__slug='institutions'),
                                         label='Учреждение', required=False)
    group = forms.ModelChoiceField(Dictionary.objects.filter(type__slug='groups'),
                                   label='Группа', required=False)
    grade = forms.ModelChoiceField(Dictionary.objects.filter(type__slug='grades'),
                                   label='Класс', required=False)

    health_states = forms.ModelMultipleChoiceField(Dictionary.objects.filter(type__slug='health'),
                                                   label='Статус здоровья', required=False)
    mode_health_states = forms.ChoiceField(label='Условия', choices=MODE_CHOICES,
                                           widget=forms.RadioSelect(), initial=0)

    parents_status = forms.ModelMultipleChoiceField(Dictionary.objects.filter(type__slug='parents'),
                                                    label='Статус родителей', required=False)
    mode_parents_status = forms.ChoiceField(label='Условия', choices=MODE_CHOICES,
                                            widget=forms.RadioSelect(), initial=0)

