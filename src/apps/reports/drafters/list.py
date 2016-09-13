#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
import xlrd
from xlutils.copy import copy
from common.utils import get_next_date, get_param_on_date
from children.functions import get_age

from django.http import HttpResponse
from children.models import Child
from itertools import groupby

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

    font = xlwt.Font()
    font.name = 'Arial Cyr'

    font_group = xlwt.Font()
    font_group.name = 'Arial Cyr'
    font_group.bold = True

    alignment = xlwt.Alignment()
    alignment.wrap = 1
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER

    alignment_group = xlwt.Alignment()
    alignment_group.wrap = 1
    alignment_group.horz = xlwt.Alignment.HORZ_LEFT
    alignment_group.vert = xlwt.Alignment.VERT_CENTER

    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN

    style = xlwt.XFStyle()
    style.font = font
    style.alignment = alignment
    style.borders = borders

    date_style = xlwt.XFStyle()
    date_style.num_format_str = "dd/mm/yyyy"
    date_style.font = font
    date_style.alignment = alignment
    date_style.borders = borders

    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['gray25']

    group_style = xlwt.XFStyle()
    group_style.font = font_group
    group_style.borders = borders
    group_style.alignment = alignment_group
    group_style.pattern = pattern

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
        sheet.write(current_row, 0, g[0], group_style)  # function age to string
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
