#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sitetree.utils import tree, item

sitetrees = (
    tree('reports', items=[
        item('Сформировать отчет', 'reports:index', in_menu=True, in_sitetree=True),
        ]),
)
