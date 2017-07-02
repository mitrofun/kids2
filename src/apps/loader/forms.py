# -*- coding: utf-8 -*-
from datetime import datetime, date
import calendar
from django import forms
from loader.validators import validate_type_file, validate_data_file


def get_last_date():
    current_date = datetime.now()
    last_date = (calendar.monthrange(current_date.year, current_date.month))[1]
    _date = date(current_date.year, current_date.month, last_date)
    return _date


class UploadFileForm(forms.Form):
    load_date = forms.DateField(label='На дату', initial=get_last_date())
    file = forms.FileField(label='Файл',
                           widget=forms.FileInput(attrs={'title': 'Выберите файл'}),
                           validators=[validate_type_file, validate_data_file]
                           )
