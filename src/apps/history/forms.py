# -*- coding: utf-8 -*-
from django import forms
from history.models import ParamHistory
from dictionaries.models import Dictionary


class HistoryForm(forms.ModelForm):
    institution = forms.ModelChoiceField(
        Dictionary.objects.filter(type__slug='institutions'),
        label='Учреждение',
        required=False
    )
    group = forms.ModelChoiceField(
        Dictionary.objects.filter(type__slug='groups'),
        label='Группа',
        required=False
    )
    grade = forms.ModelChoiceField(
        Dictionary.objects.filter(type__slug='grades'),
        label='Класс',
        required=False
    )
    parents_status = forms.ModelMultipleChoiceField(
        Dictionary.objects.filter(type__slug='parents'),
        label='Статус родителей',
        required=False
    )
    health_states = forms.ModelMultipleChoiceField(
        Dictionary.objects.filter(type__slug='health'),
        label='Состояние здоровья',
        required=False
    )

    class Meta:
        model = ParamHistory
        fields = [
            'first_date',
            'last_date',
            'child',
            'parameter',
            'institution',
            'group',
            'grade',
            'parents_status',
            'health_states',
            'risk_group',
            'note'
        ]
