#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from parameters.models import HealthHistory
from dictionaries.models import Dictionary


class HealthHistoryForm(forms.ModelForm):
    states = forms.ModelChoiceField(Dictionary.objects.filter(type__slug='health'), label='Состояние', required=False)

    class Meta:
        model = HealthHistory
        fields = [
            'first_date',
            'last_date',
            'child',
            'states'
        ]
