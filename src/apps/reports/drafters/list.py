#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
from xlutils.copy import copy
from common.utils import get_next_date, get_param_on_date, get_display_age
from children.functions import get_age

from django.http import HttpResponse
from children.models import Child
from itertools import groupby
from reports.drafters.styles import style, group_style, date_style

content_type = 'application/vnd.ms-excel'
report_template_dir = 'src/apps/reports/templates/list.xls'


def report(on_date):

    children_list = []

    first_row = 3
    next_date = get_next_date(on_date)
    response = HttpResponse(content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename=list({}).xls'.format(next_date)

    rb = xlrd.open_workbook(report_template_dir, formatting_info=True)
    wb = copy(rb)
    sheet = wb.get_sheet(0)

    children = Child.objects.all()

    for child in children:
        children_list.append([
            get_age(child.birthday, on_date=on_date),
            child.last_name,
            child.first_name,
            child.middle_name,
            child.birthday,
            child.locality.name,
            child.street.name,
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

    current_row = first_row
    for g in groupby(sorted(children_list, key=lambda x: x[0]), key=lambda x: x[0]):
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
