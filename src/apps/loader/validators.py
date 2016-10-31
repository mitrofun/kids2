#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
from django.conf import settings
from django.core.exceptions import ValidationError
from children.models import Child
from dictionaries.models import Dictionary
import pyexcel


def _validate_excel_data(file_data):

    list__error = []
    for item in file_data:

        number = item[0]
        birthday = item[4]
        locality = item[5]
        street = item[6]
        institution = item[9]
        group = item[10]
        grade = item[11]
        health = item[12]
        parent = item[13]

        if birthday == '':
            list__error.append('В строке c номером п/п {number} отсутствует дата'.format(number=number))
        if not isinstance(birthday, datetime.date):
            list__error.append('В строке c номером п/п {number} не верный формат даты - {date}'.
                               format(number=number, date=birthday)
                               )

        try:
            Dictionary.objects.get(type__slug='locality', name=locality)
        except Dictionary.DoesNotExist:
            if locality == '':
                text_error = 'В строке c номером п/п {number} не указан населенный пункт'.\
                    format(number=number)
            else:
                text_error = 'В строке c номером п/п {number} указан населенный пункт отсутствующий в ' \
                             'справочнике - {locality}'.format(number=number, locality=locality)
            list__error.append(text_error)

        if street:
            try:
                Dictionary.objects.get(type__slug='streets', name=street)
            except Dictionary.DoesNotExist:
                    text_error = 'В строке c номером п/п {number} указана улица отсутствующая в ' \
                                 'справочнике - {street}'.format(number=number, street=street)
                    list__error.append(text_error)

        if institution:
            try:
                Dictionary.objects.get(type__slug='institutions', name=institution)
            except Dictionary.DoesNotExist:
                text_error = 'В строке c номером п/п {number} указано учреждение отсутствующее в ' \
                                 'справочнике - {institution}'.format(number=number, institution=institution)
                list__error.append(text_error)

        if group:
            try:
                Dictionary.objects.get(type__slug='groups', name=group)
            except Dictionary.DoesNotExist:
                    text_error = 'В строке c номером п/п {number} указана возрастная группа отсутствующая в ' \
                                 'справочнике - {group}'.format(number=number, group=group)
                    list__error.append(text_error)

        if grade:
            try:
                Dictionary.objects.get(type__slug='grades', name=grade)
            except Dictionary.DoesNotExist:
                text_error = 'В строке c номером п/п {number} указан класс отсутствующий в ' \
                             'справочнике - {grade}'.format(number=number, grade=grade)
                list__error.append(text_error)

        if health:
            health_list = health.replace(' ', '').split(',')
            for value in health_list:
                if value:
                    try:
                        Dictionary.objects.get(type__slug='health', name=value)
                    except Dictionary.DoesNotExist:
                        text_error = 'В строке c номером п/п {number} указано состаяние здоровья отсутствующее в ' \
                                     'справочнике - {value}'.format(number=number, value=value)
                        list__error.append(text_error)

        if parent:
            parent_list = parent.replace(' ', '').split(',')
            for value in parent_list:
                if value:
                    try:
                        Dictionary.objects.get(type__slug='parents', name=value)
                    except Dictionary.DoesNotExist:
                        text_error = 'В строке c номером п/п {number} указан статус родителей отсутствующей в ' \
                                     'справочнике - {value}'.format(number=number, value=value)
                        list__error.append(text_error)

    return list__error


def _validate_prev_data_in_file(file_data):
    list__error = []
    contain_need_data = []

    for item in file_data:
        if isinstance(item[4], datetime.date):
            contain_need_data.append(True)
        try:
            Child.objects.get(
                last_name=item[1],
                first_name=item[2],
                middle_name=item[3]
            )
            contain_need_data.append(True)
        except Child.DoesNotExist:
            pass

    if contain_need_data:
        list__error.append('Данные в файле должны начинаться со строки {number}'.
                           format(number=settings.EXCEL_START_STRING + 1)
                           )

    return list__error


def validate_type_file(file):
    ext = os.path.splitext(file.name)[1]
    valid_extensions = ['.xlsx', '.xls', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Не поддерживается тип файла, можно загружать только файлы excel')


def validate_data_file(file):

    tmp_file = open('{}/{}'.format(settings.MEDIA_ROOT, file), 'wb')
    tmp_file.write(file.read())
    tmp_file.close()

    file_data = pyexcel.get_array(file_name="{}/{}".format(settings.MEDIA_ROOT, file))

    list_error = []

    list_error += _validate_prev_data_in_file(file_data[: settings.EXCEL_START_STRING])
    list_error += _validate_excel_data(file_data[settings.EXCEL_START_STRING:])

    if len(list_error):
        text = ['В файе присутствуют ошибки:'] + list_error
        raise ValidationError(text)
