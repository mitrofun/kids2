#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('parameters/educations/_child_education_list.html')
def child_education_history(child, education_list):
    return {
        'child': child,
        'education_list': education_list
    }
