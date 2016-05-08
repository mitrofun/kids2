#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sitetree.utils import tree, item

sitetrees = (
    tree('children_tree', items=[
        item('Дети', 'children:list', children=[
            item('Добавить', 'children:add', in_menu=False, in_sitetree=False),
            item('{{ child }}', 'children:detail child.id', in_menu=False,
                 in_sitetree=False, children=[
                    item('Редактировать', 'children:edit child.id', in_menu=False,
                         in_sitetree=False),
                    item('Удалить', 'children:edit child.id', in_menu=False, in_sitetree=False)
                ]),
        ]),
        item('Фильтр', 'children:filter', in_menu=False, in_sitetree=False),
    ]),
)
