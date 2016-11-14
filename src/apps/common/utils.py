#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import timedelta
from dictionaries.models import Dictionary
from history.models import ParamHistory
from django.db.models import Q
from children.functions import get_age
from children.models import Child


def get_list_age():

    ages = []
    ages.extend(range(1, 7))
    ages.extend([6.6])
    ages.extend(range(7, 20))

    return ages


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

        if parameter == 'institution_id':
            if all_history[0].institution is not None:
                return all_history[0].institution.id
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


def get_display_age(age):

    if age == 1:
        return '{} год'.format(age)
    elif age in range(2, 5):
        return '{} года'.format(age)
    elif age in range(5, 19):
        return '{} лет'.format(age)
    elif age == 6.6:
        return '6 лет 6м'
    elif age > 18:
        return 'старше 18 лет'
    else:
        return 'проверте дату рождения'


def get_institution(institution_type=None):

    institution_qs = Dictionary.objects.filter(type__slug='institutions', ).order_by('institution_type', 'name')
    if institution_type is not None:
        institution_qs = institution_qs.filter(institution_type=institution_type)

    return institution_qs


def get_children_institution_list_on_date(date):

    children_list = []

    children = Child.objects.all()

    for child in children:
        children_list.append([
            get_age(child.birthday, on_date=date),
            get_param_on_date(child, 'education', 'institution_id', date),
        ])

    return children_list


def get_children_count_by_list(children_list, institution_id, age, consider_institution=True):

    if age <= 18:
        _children_list = list(filter(lambda el: el[0] == age, children_list))
    else:
        _children_list = list(filter(lambda el: el[0] > 18, children_list))

    if _children_list:
        if consider_institution:
            if institution_id is not None:
                __children_list = list(filter(lambda el: el[1] == institution_id, _children_list))
            else:
                __children_list = list(filter(lambda el: el[1] is None, _children_list))
            return len(__children_list)
        else:
            return len(_children_list)
    else:
        return 0
