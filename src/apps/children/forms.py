#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from children.models import Child
from dictionaries.models import Dictionary


class ChildForm(forms.ModelForm):
    birthday = forms.CharField(label='Дата рождения',
                               widget=forms.TextInput(attrs={'type': 'date'}))
    locality = forms.ModelChoiceField(Dictionary.objects.all(), empty_label=None, label='Населенный пункт')
    street = forms.ModelChoiceField(Dictionary.objects.all(), empty_label=None, label='Улица')

    class Meta:
        model = Child
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'birthday',
            'locality',
            'street',
            'house',
            'flat'
        ]
