#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('children/tabs/_education_list.html')
def child_education_history(child, education_list):
    return {
        'child': child,
        'education_list': education_list
    }


@register.inclusion_tag('children/tabs/_health_list.html')
def child_health_history(child, health_list):
    return {
        'child': child,
        'health_list': health_list
    }


@register.inclusion_tag('children/tabs/_note_list.html')
def child_note_history(child, education_list):
    return {
        'child': child,
        'note_list': education_list
    }


@register.inclusion_tag('children/tabs/_parent_list.html')
def child_parent_history(child, parent_list):
    return {
        'child': child,
        'parent_list': parent_list
    }


@register.inclusion_tag('children/tabs/_risk_list.html')
def child_risk_history(child, education_list):
    return {
        'child': child,
        'risk_list': education_list
    }
