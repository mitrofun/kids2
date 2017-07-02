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
                    item('Редактировать {{param.name}}', 'children:history-edit child.id param.slug history.id',
                         in_menu=False, in_sitetree=False),
                    item('Удалить {{param.name}}', 'children:history-delete child.id param.slug history.id',
                         in_menu=False, in_sitetree=False),
                ]),

                ]),

        ]),
)
