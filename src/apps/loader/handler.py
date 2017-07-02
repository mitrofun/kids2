# -*- coding: utf-8 -*-
from children.models import Child
from history.models import ParamHistory, Param
from common.utils import get_dictionary_item


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

    child.locality = get_dictionary_item(locality, 'locality')
    child.street = get_dictionary_item(street, 'streets')
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


def set_children_m2m_param(param_type, child, date, values):

    try:
        parameter = Param.objects.get(slug=param_type)
        values = values.replace(' ', '').split(',')
        if date_is_free(child, param_type, date) and values_is_in_dictionary(values, param_type):

            history = ParamHistory.objects.create(
                first_date=date,
                parameter=parameter,
                child=child,
                risk_group=0
            )

            for value in values:
                dict_value = get_dictionary_item(value, param_type)
                if dict_value:
                    if param_type == 'health':
                        history.health_states.add(dict_value)
                    if param_type == 'parents':
                        history.parents_status.add(dict_value)

    except Param.DoesNotExist:
        pass


def set_children_simple_param(param_type, child, date, value):
    try:
        parameter = Param.objects.get(slug=param_type)

        if param_type == 'risk':
            value = list(filter(lambda val_list: val_list[1] == value, ParamHistory.BOOL_CHOICES))

        if date_is_free(child, param_type, date) and value:
            if param_type == 'risk':
                ParamHistory.objects.create(
                    first_date=date,
                    parameter=parameter,
                    child=child,
                    risk_group=value[0]
                )
            else:
                ParamHistory.objects.create(
                    first_date=date,
                    parameter=parameter,
                    child=child,
                    risk_group=0,
                    note=value
                )

    except Param.DoesNotExist:
        pass


def loader(data, on_date):

    for item in data:
        child = get_child(item)
        set_children_address(child, item)
        set_children_education(child, on_date, item)
        set_children_m2m_param('health', child, on_date, item[12])
        set_children_m2m_param('parents', child, on_date, item[13])
        set_children_simple_param('risk', child, on_date, item[14])
        set_children_simple_param('note', child, on_date, item[15])
