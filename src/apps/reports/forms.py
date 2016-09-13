#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, date
import calendar
from django import forms


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

    report_date = forms.DateField(label='Дата', initial=get_last_date())
    report_type = forms.ChoiceField(label='Тип отчета', choices=REPORT_CHOICES)
