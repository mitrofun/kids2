# -*- coding: utf-8 -*-
from django import template
from common.utils import get_display_age
from history.helper import PARAM_ACCORDANCE
from common.utils import get_param_on_date
import datetime


register = template.Library()


@register.inclusion_tag('history/partials/_list.html')
def get_history(child, params, param_type):
    titles = []
    param_list = list(filter(lambda x: x.parameter.slug == param_type, params))
    for setting in PARAM_ACCORDANCE:
        if setting['name'] == param_type:
            titles.extend(setting['title'])
    return {
        'child': child,
        'params': param_list,
        'param_type': param_type,
        'title_list': titles
    }


@register.inclusion_tag('history/partials/_last_education.html')
def get_last_education(child):

    current_education = get_param_on_date(child=child, parameter_type='education',
                                          parameter='', date=datetime.date.today())

    return {
        'last_education': current_education,
    }


@register.filter
def display_age(age):
    return get_display_age(age)
