#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from history.models import ParamHistory
from history.helper import PARAM_ACCORDANCE

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
    last_education = ParamHistory.objects.filter(child=child).filter(parameter__slug='education').last()
    return {
        'last_education': last_education,
    }

