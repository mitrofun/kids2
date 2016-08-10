#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from parameters.models import StudentHistory
from dictionaries.models import Dictionary


class EducationHistoryForm(forms.ModelForm):
    institution = forms.ModelChoiceField(Dictionary.objects.filter(type__slug='institutions'),
                                         label='Учреждение', required=False)
    group = forms.ModelChoiceField(Dictionary.objects.filter(type__slug='groups'), label='Группа', required=False)
    grade = forms.ModelChoiceField(Dictionary.objects.filter(type__slug='grades'), label='Класс', required=False)

    class Meta:
        model = StudentHistory
        fields = [
            'first_date',
            'last_date',
            'child',
            'institution',
            'group',
            'grade'
        ]
