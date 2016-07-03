#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sitetree.utils import tree, item

sitetrees = (
    tree('dictionaries_tree', items=[

        item('Справочники', 'dictionaries', children=[
            item('Образование', 'education', in_menu=True, in_sitetree=True,  children=[
                item('Учреждения', 'institutions:list', in_menu=True, in_sitetree=True,  children=[
                    item('Добавить', 'institutions:add', in_menu=False, in_sitetree=False),
                    item('{{ institution }}', 'institutions:detail institution.id', in_menu=True,
                         in_sitetree=True, children=[
                            item('Редактировать', 'institutions:edit institution.id', in_menu=False, in_sitetree=False),
                            item('Удалить', 'institutions:delete institution.id', in_menu=False, in_sitetree=False),
                    ])
                ]),
                item('Возрастные группы', 'groups:list', in_menu=True, in_sitetree=True,  children=[
                    item('Добавить', 'groups:add', in_menu=False, in_sitetree=False),
                    item('{{ group }}', 'groups:detail group.id', in_menu=False, in_sitetree=False, children=[
                        item('Редактировать', 'groups:edit group.id', in_menu=False, in_sitetree=False),
                        item('Удалить', 'groups:delete group.id', in_menu=False, in_sitetree=False),
                    ])
                ]),
                item('Классы', '', in_menu=True, in_sitetree=True,  children=[
                    # item('Добавить', '', in_menu=False, in_sitetree=False),
                    # item('Учреждение', '', in_menu=False, in_sitetree=False, children=[
                    #     item('Редактировать', '', in_menu=False, in_sitetree=False),
                    #     item('Удалить', '', in_menu=False, in_sitetree=False),
                    # ])
                ])
            ]),
            # item('Адреса', '', in_menu=True, in_sitetree=True, children=[
            #     item('Населенные пункты', '', in_menu=True, in_sitetree=True, children=[]),
            #     item('Улицы', '', in_menu=True, in_sitetree=True, children=[]),
            # ]),
            # item('Дополнительные данные', '', in_menu=True, in_sitetree=True, children=[
            #     item('Состояния здоровья', '', in_menu=True, in_sitetree=True, children=[]),
            #     item('Статусы родителей', '', in_menu=True, in_sitetree=True, children=[]),
            # ]),
        ]),
        # item('Сформировать отчет', '', in_menu=True, in_sitetree=True),
        # item('Загрузить данные', '', in_menu=True, in_sitetree=True),
        # item('Фильтр', 'children:filter', in_menu=False, in_sitetree=False),
    ]),
)
