#!/usr/bin/env python
# -*- coding: utf-8 -*-
from children.models import Child
from dictionaries.models import Dictionary
from history.models import ParamHistory


def get_dictionary_item(type_name, value):
    try:
        result = Dictionary.objects.get(type__slug=type_name, name=value)
    except Dictionary.DoesNotExist:
        result = ''
    return result


def set_children_address(child, *args):

    _, _, _, _, _, locality, street, house, flat, _ = args

    child.locality = get_dictionary_item('locality', locality)
    child.street = get_dictionary_item('streets', street)
    child.house = house
    child.flat = flat
    child.save()


def get_child(*args):
    _, last_name, first_name, middle_name, birthday, _ = args

    child, created = Child.objects.get_or_create(
        last_name=last_name,
        first_name=first_name,
        middle_name=middle_name,
        birthday=birthday)

    return child


def set_children_education(child, date, *args):
    institution = args[9]
    group = args[10]
    grade = args[11]
    pass


def set_children_other_data(child, date, *args):
    health_states = args[12]
    parents_status = args[13]
    risk_group = args[14]
    note = args[15]
    pass


def loader(data, on_date):
    print(on_date)
    for item in data:
        child = get_child(item)
        set_children_address(child, item)
        # set_children_education(child, on_date, item)
        # set_children_other_data(child, on_date, item)
