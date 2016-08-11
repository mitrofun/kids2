#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sitetree.utils import tree, item

sitetrees = (
    tree('children', items=[

        item('Дети', 'children:list', children=[
            item('Добавить', 'children:add', in_menu=False, in_sitetree=False),
            item('{{ child }}', 'children:detail child.id', in_menu=False,
                 in_sitetree=False, children=[
                    item('Редактировать', 'children:edit child.id', in_menu=False,
                         in_sitetree=False),
                    item('Удалить', 'children:edit child.id', in_menu=False, in_sitetree=False),

                    item('Добавить {{param.name}}', 'children:history-add child.id param.slug',
                         in_menu=False, in_sitetree=False),
                ]),

                ]),

        ]),
)
