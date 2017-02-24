#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from children.functions import get_last_date
from dictionaries.models import Dictionary


class FilterForm(forms.Form):

    MODE_CHOICES = [(0, 'С любым статусом из списка'),
                    (1, 'Такие статусы входят в условие'),
                    (2, 'Только все эти статусы')]

    report_date = forms.DateField(label='Дата', initial=get_last_date())

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
