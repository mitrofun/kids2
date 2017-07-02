# -*- coding: utf-8 -*-
import xlwt

FONT = 'Arial Cyr'


font = xlwt.Font()
font.name = FONT

font_group = xlwt.Font()
font_group.name = FONT
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

pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlwt.Style.colour_map['gray25']

# styles

style = xlwt.XFStyle()
style.font = font
style.alignment = alignment
style.borders = borders

style_bold = xlwt.XFStyle()
style_bold.font = font_group
style_bold.alignment = alignment
style_bold.borders = borders

date_style = xlwt.XFStyle()
date_style.num_format_str = "dd/mm/yyyy"
date_style.font = font
date_style.alignment = alignment
date_style.borders = borders

group_style = xlwt.XFStyle()
group_style.font = font_group
group_style.borders = borders
group_style.alignment = alignment_group
group_style.pattern = pattern
