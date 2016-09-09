#!/usr/bin/env python
# -*- coding: utf-8 -*-
from children.models import Child
from dictionaries.models import Dictionary
from history.models import ParamHistory, Param


def get_dictionary_item(value, type_name):

    try:
        result = Dictionary.objects.get(type__slug=type_name, name=value)
    except Dictionary.DoesNotExist:
        result = None
    return result


def values_is_in_dictionary(values_list, type_name):

    for value in values_list:
        if get_dictionary_item(value, type_name):
            return True

    return False


def set_children_address(child, args):

    locality = args[5]
    street = args[6]
    house = args[7]
    flat = args[8]

    child.locality = get_dictionary_item('locality', locality)
    child.street = get_dictionary_item('streets', street)
    child.house = house
    child.flat = flat
    child.save()


def get_child(args):

    last_name = args[1]
    first_name = args[2]
    middle_name = args[3]
    birthday = args[4]

    child, created = Child.objects.get_or_create(
        last_name=last_name,
        first_name=first_name,
        middle_name=middle_name,
        birthday=birthday)

    return child


def date_is_free(child, parameter, date):
    return not ParamHistory.objects.filter(child=child, parameter__slug=parameter, first_date=date)


def set_children_education(child, date, args):

    institution = args[9]
    group = args[10]
    grade = args[11]

    try:
        parameter = Param.objects.get(slug='education')

        if date_is_free(child, 'education', date):

            ParamHistory.objects.create(
                first_date=date,
                parameter=parameter,
                child=child,
                institution=get_dictionary_item(institution, 'institutions'),
                group=get_dictionary_item(group, 'groups'),
                grade=get_dictionary_item(grade, 'grades'),
                risk_group=0
            )

    except Param.DoesNotExist:
        pass


def set_children_health_states(child, date, values):

    try:
        parameter = Param.objects.get(slug='health')
        values = values.replace(' ', '').split(',')

        if date_is_free(child, 'health', date) and values_is_in_dictionary(values, 'health'):

            history = ParamHistory.objects.create(
                first_date=date,
                parameter=parameter,
                child=child,
                risk_group=0
            )

            for value in values:
                health_state = get_dictionary_item(value, 'health')
                if health_state:
                    history.health_states.add(health_state)

    except Param.DoesNotExist:
        pass


def loader(data, on_date):

    for item in data:
        child = get_child(item)
        set_children_address(child, item)
        set_children_education(child, on_date, item)
        set_children_health_states(child, on_date, item[12])
