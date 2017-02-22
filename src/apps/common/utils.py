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


def get_qs_by_param_name(date, qs, name, **kwargs):

    _children_qs = ParamHistory.objects. \
        filter(first_date__lt=date). \
        filter(Q(last_date__lte=date) | Q(last_date__isnull=True))

    if name == 'institution':
        _children_qs = _children_qs.filter(institution=kwargs['institution'])
    if name == 'group':
        _children_qs = _children_qs.filter(group=kwargs['group'])
    if name == 'grade':
        _children_qs = _children_qs.filter(grade=kwargs['grade'])
    if name == 'parents_status':
        _children_qs = _children_qs.filter(parents_status__in=kwargs['parents_status'])
    if name == 'health_states':
        _children_qs = _children_qs.filter(health_states__in=kwargs['health_states'])

    _children_list = _children_qs.values_list('child_id', flat=True)

    if _children_list:
        qs = qs.filter(pk__in=set(_children_list))
    else:
        qs = qs.none()

    return qs


def get_children_institution_list_on_date(date, **kwargs):

    health_states = kwargs['health_states']
    mode_health_states = int(kwargs['mode_health_states'])
    parents_status = kwargs['parents_status']
    mode_parents_status = int(kwargs['mode_parents_status'])

    children_list = []

    children_qs = Child.objects.all()

    if health_states:
        children_qs = get_qs_by_param_name(date=date, name='health_states', qs=children_qs, **kwargs)

    if parents_status:
        children_qs = get_qs_by_param_name(date=date, name='parents_status', qs=children_qs, **kwargs)

    for child in children_qs:
        children_list.append([
            get_age(child.birthday, on_date=date),
            get_param_on_date(child, 'education', 'institution_id', date),
            get_param_on_date(child, 'health', 'health_list', date),
            get_param_on_date(child, 'parents', 'parents_list', date),
        ])

    if health_states and mode_health_states != 0:

        _children_list = children_list.copy()
        children_list.clear()

        if mode_health_states == 2:

            _condition = ', '.join([states.name for states in health_states])
            for _children in _children_list:
                if _children[2] == _condition:
                    children_list.append(_children)
        else:

            _condition = [states.name for states in health_states]
            for _children in _children_list:

                if set(_condition) <= set(_children[2].split(', ')):
                    children_list.append(_children)

    if parents_status and mode_parents_status != 0:

        _children_list = children_list.copy()
        children_list.clear()

        if mode_parents_status == 2:

            _condition = ', '.join([status.name for status in parents_status])
            for _children in _children_list:
                if _children[3] == _condition:
                    children_list.append(_children)
        else:

            _condition = [status.name for status in parents_status]
            for _children in _children_list:

                if set(_condition) <= set(_children[3].split(', ')):
                    children_list.append(_children)

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
