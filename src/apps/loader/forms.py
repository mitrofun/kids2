#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms


class UploadFileForm(forms.Form):
    load_date = forms.DateField(label='На дату')
    file = forms.FileField(label='Файл')
