#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from history.models import ParamHistory

register = template.Library()


@register.inclusion_tag('history/partials/_list.html')
def get_history(child, params, param_type):
    return {
        'child': child,
        'params': params,
        'param_type': param_type
    }


@register.inclusion_tag('history/partials/_last_education.html')
def get_last_education(child):
    last_education = ParamHistory.objects.filter(child=child).filter(parameter__slug='education').last()
    return {
        'last_education': last_education,
    }

