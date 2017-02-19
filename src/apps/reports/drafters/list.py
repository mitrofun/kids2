#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
from xlutils.copy import copy
from common.utils import get_next_date, get_param_on_date, get_display_age
from children.functions import get_age
from django.db.models import Q
from django.http import HttpResponse
from children.models import Child
from history.models import ParamHistory
from itertools import groupby
from reports.drafters.styles import style, group_style, date_style

content_type = 'application/vnd.ms-excel'
report_template_dir = 'src/apps/reports/templates/list.xls'


def report(**kwargs):

    on_date = kwargs['report_date']
    institution = kwargs['institution']
    group = kwargs['group']
    grade = kwargs['grade']
    health_states = kwargs['health_states']
    mode_health_states = int(kwargs['mode_health_states'])
    parents_status = kwargs['parents_status']
    mode_parents_status = int(kwargs['mode_parents_status'])

    children_list = []

    first_row = 3
    next_date = get_next_date(on_date)
    response = HttpResponse(content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename=list({}).xls'.format(next_date)

    rb = xlrd.open_workbook(report_template_dir, formatting_info=True)
    wb = copy(rb)
    sheet = wb.get_sheet(0)

    children_qs = Child.objects.all()

    if institution:

        _children_list = ParamHistory.objects. \
            filter(first_date__lt=on_date). \
            filter(Q(last_date__lte=on_date) | Q(last_date__isnull=True)). \
            filter(institution=institution). \
            values_list('child_id', flat=True)

        if _children_list:
            children_qs = Child.objects.filter(pk__in=set(_children_list))

    if group:

        _children_list = ParamHistory.objects. \
            filter(first_date__lt=on_date). \
            filter(Q(last_date__lte=on_date) | Q(last_date__isnull=True)). \
            filter(group=group). \
            values_list('child_id', flat=True)

        if _children_list:
            children_qs = children_qs.filter(pk__in=set(_children_list))
        else:
            children_qs = children_qs.none()

    if grade:

        _children_list = ParamHistory.objects. \
            filter(first_date__lt=on_date). \
            filter(Q(last_date__lte=on_date) | Q(last_date__isnull=True)). \
            filter(grade=grade). \
            values_list('child_id', flat=True)

        # print(children_qs.query)

        if _children_list:
            children_qs = children_qs.filter(pk__in=set(_children_list))
        else:
            children_qs = children_qs.none()

    if health_states:

        _children_list = ParamHistory.objects.\
            filter(first_date__lt=on_date).\
            filter(Q(last_date__lte=on_date) | Q(last_date__isnull=True)).\
            filter(health_states__in=health_states). \
            values_list('child_id', flat=True)

        if _children_list:
            children_qs = children_qs.filter(pk__in=set(_children_list))
        else:
            children_qs = children_qs.none()

    if parents_status:

        _children_list = ParamHistory.objects.\
            filter(first_date__lt=on_date).\
            filter(Q(last_date__lte=on_date) | Q(last_date__isnull=True)).\
            filter(parents_status__in=parents_status). \
            values_list('child_id', flat=True)

        if _children_list:
            children_qs = children_qs.filter(pk__in=set(_children_list))
        else:
            children_qs = children_qs.none()

    if not institution and not group and not grade and not health_states and not parents_status:
        children_qs = Child.objects.all()

    # print(children_qs)
    # print(children_qs.query)

    for child in children_qs:
        if child.street:
            street = child.street.name
        else:
            street = ''

        children_list.append([
            get_age(child.birthday, on_date=on_date),
            child.last_name,
            child.first_name,
            child.middle_name,
            child.birthday,
            child.locality.name,
            street,
            child.house,
            child.flat,
            get_param_on_date(child, 'education', 'institution_name', on_date),
            get_param_on_date(child, 'education', 'group_name', on_date),
            get_param_on_date(child, 'education', 'grade_name', on_date),
            get_param_on_date(child, 'health', 'health_list', on_date),
            get_param_on_date(child, 'parents', 'parents_list', on_date),
            get_param_on_date(child, 'risk', 'display_risk', on_date),
            get_param_on_date(child, 'note', 'display_note', on_date),
        ])

    if health_states and mode_health_states != 0:

        # print(health_states)
        # print(mode_health_states)

        _children_list = children_list.copy()
        children_list.clear()

        if mode_health_states == 2:

            _condition = ', '.join([states.name for states in health_states])
            for _children in _children_list:
                if _children[13] == _condition:
                    children_list.append(_children)
        else:

            _condition = [states.name for states in health_states]
            for _children in _children_list:

                if set(_condition) <= set(_children[13].split(', ')):
                    children_list.append(_children)

    if parents_status and mode_parents_status != 0:

        _children_list = children_list.copy()
        children_list.clear()

        if mode_parents_status == 2:

            _condition = ', '.join([status.name for status in parents_status])
            for _children in _children_list:
                if _children[13] == _condition:
                    children_list.append(_children)
        else:

            _condition = [status.name for status in parents_status]
            for _children in _children_list:

                if set(_condition) <= set(_children[13].split(', ')):
                    children_list.append(_children)

    # print(children_list)

    children_list.sort(key=lambda x: (x[0], x[1]))

    current_row = first_row
    for g in groupby(children_list, key=lambda x: x[0]):
        sheet.write_merge(current_row, current_row, 0, 15, style=group_style)
        sheet.write(current_row, 0, get_display_age(g[0]), group_style)
        for i, child in enumerate(g[1]):
            current_row += 1
            i += 1
            sheet.write(current_row, 0, i, style)
            for a in range(1, 16):
                if a == 4:
                    sheet.write(current_row, a, child[a], date_style)
                else:
                    sheet.write(current_row, a, child[a], style)

        current_row += 1

    wb.save(response)

    return response
