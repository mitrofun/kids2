#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from common.forms import FilterForm


class ReportsForm(FilterForm):

    field_order = ['report_date', 'report_type', ]

    REPORT_CHOICES = (
        (1, 'Список'),
        (2, 'Свод')
    )
    report_type = forms.ChoiceField(label='Тип отчета', choices=REPORT_CHOICES)

