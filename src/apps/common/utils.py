#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import timedelta
from dictionaries.models import Dictionary
from history.models import ParamHistory
from django.db.models import Q


def get_next_date(date):
    """
    Возвращаем следующую дату, за отправленной
    :param date: Дата
    :return: Следующий день, type = date
    """
    return date + timedelta(days=1)


def get_dictionary_item(value, type_name):

    try:
        result = Dictionary.objects.get(type__slug=type_name, name=value)
    except Dictionary.DoesNotExist:
        result = None
    return result


def get_param_on_date(child, parameter_type, parameter, date):

    all_history = ParamHistory.objects.filter(child=child, parameter__slug=parameter_type).\
        filter(first_date__lte=date).filter(Q(last_date__gte=date) | Q(last_date__isnull=True)).order_by('last_date')

    if all_history:

        if parameter == '':
            return all_history[0]

        if parameter == 'institution_name':
            if all_history[0].institution is not None:
                return all_history[0].institution.name
            else:
                return None

        if parameter == 'group_name':
            if all_history[0].group is not None:
                return all_history[0].group.name
            else:
                return None

        if parameter == 'grade_name':
            if all_history[0].grade is not None:
                return all_history[0].grade.name
            else:
                return None

        if parameter == 'health_list':

            if all_history[0].health_states is not None:
                return all_history[0].get_health_states()
            else:
                return None

        if parameter == 'parents_list':

            if all_history[0].parents_status is not None:
                return all_history[0].get_parents_status()
            else:
                return None

        if parameter == 'display_risk':

            if all_history[0].parents_status is not None:
                return all_history[0].get_risk_group_display()
            else:
                return None

        if parameter == 'display_note':

            if all_history[0].parents_status is not None:
                return all_history[0].note
            else:
                return None

    else:
        return None
