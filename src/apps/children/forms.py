# -*- coding: utf-8 -*-
from django import forms
from children.models import Child
from common.forms import FilterForm
from dictionaries.models import Dictionary


class ChildForm(forms.ModelForm):
    locality = forms.ModelChoiceField(
        Dictionary.objects.filter(type__slug='locality'),
        empty_label=None,
        label='Населенный пункт'
    )
    street = forms.ModelChoiceField(
        Dictionary.objects.filter(type__slug='streets'),
        label='Улица'
    )

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


class FilterChildrenForm(FilterForm):
    field_order = ['report_date', ]
