# -*- coding: utf-8 -*-
import xlrd
from django_rq import job
from xlwt import Formula, Utils
from xlutils.copy import copy
from common.utils import get_institution, get_list_age, \
    get_children_institution_list_on_date, get_children_count_by_list
from django.http import HttpResponse
from reports.drafters.styles import style, style_bold


FIRST_ROW = 2
FIRST_COLUMN = 0


do_title = 'Дошкольные образовательные организации, из них'
full_title = 'Общеобразовательные организации, из них'
minor_title = 'Несовершеннолетние, не посещающие образовательные организации'

content_type = 'application/vnd.ms-excel'
report_template_dir = 'src/apps/reports/templates/summary.xls'


def write_text(sheet, title, col, row, _style):
    sheet.write(col, row, title, _style)


def write_head(sheet):

    c_row = FIRST_ROW
    c_col = FIRST_COLUMN

    write_text(sheet, do_title, c_col, c_row, style_bold)
    c_row += 1

    for institution in get_institution(0):
        sheet.write(c_col, c_row, institution.name, style)
        c_row += 1

    write_text(sheet, full_title, c_col, c_row, style_bold)
    c_row += 1

    for institution in get_institution(1):
        sheet.write(c_col, c_row, institution.name, style)
        c_row += 1

    write_text(sheet, minor_title, c_col, c_row, style)


def write_data_by_institution(sheet, col, row, institution_id, children_list):

    for age in get_list_age():
        sheet.write(col, row,
                    get_children_count_by_list(children_list, institution_id, age), style)
        col += 1


def write_table(sheet, on_date, **kwargs):

    c_row = FIRST_ROW + 1
    c_col = FIRST_COLUMN + 1

    _children_list = get_children_institution_list_on_date(on_date, **kwargs)

    for institution in get_institution(0):
        write_data_by_institution(sheet, c_col, c_row, institution.id, _children_list)
        c_row += 1

    # todo: удалить не нужное из списка с типом 0  при оптимизации

    for institution in get_institution(1):
        write_data_by_institution(sheet, c_col, c_row + 1, institution.id, _children_list)
        c_row += 1

    # todo: удалить не нужное из списка с типом 1 учреждений при оптимизации

    write_data_by_institution(sheet, c_col, c_row + 1, None, _children_list)


def write_total(sheet):
    count_ages = 20
    col = FIRST_COLUMN + 1
    row = FIRST_ROW
    count_do = get_institution(0).count()
    count_school = get_institution(1).count()
    count_row = get_institution().count() + 3

    for i, age in enumerate(get_list_age()):
        formula_do = 'SUM({}:{})'.format(
            Utils.rowcol_to_cell(row - 1 + i, col + 2),
            Utils.rowcol_to_cell(row - 1 + i, col + 1 + count_do)
        )
        formula_school = 'SUM({}:{})'.format(
            Utils.rowcol_to_cell(row - 1 + i, col + 2 + count_do + 1),
            Utils.rowcol_to_cell(row - 1 + i, col + 2 + count_do + count_school)
        )
        formula_total_row = '{} + {} + {}'.format(
            Utils.rowcol_to_cell(row - 1 + i, col + 1),
            Utils.rowcol_to_cell(row - 1 + i, col + 1 + count_do + 1),
            Utils.rowcol_to_cell(row - 1 + i, col + 1 + count_do + 2 + count_school),
        )
        sheet.write(col + i, row - 1, Formula(formula_total_row), style_bold)
        sheet.write(col + i, row, Formula(formula_do), style_bold)
        sheet.write(col + i, row + count_do + 1, Formula(formula_school), style_bold)

    for j in range(count_row + 1):
        formula_total_col = 'SUM({}:{})'.format(
            Utils.rowcol_to_cell(row - 1, col + j),
            Utils.rowcol_to_cell(row - 1 + count_ages - 1, col + j)
        )
        sheet.write(col + count_ages, row - 1 + j, Formula(formula_total_col), style_bold)


@job
def report(**kwargs):
    on_date = kwargs['report_date']

    response = HttpResponse()

    rb = xlrd.open_workbook(report_template_dir, formatting_info=True)
    wb = copy(rb)
    sheet = wb.get_sheet(0)

    write_head(sheet)
    write_table(sheet, on_date, **kwargs)
    write_total(sheet)

    wb.save(response)

    return response
