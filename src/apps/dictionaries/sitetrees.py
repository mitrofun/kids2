#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sitetree.utils import tree, item

sitetrees = (
    tree('dictionaries', items=[
        item('Справочники', 'dictionaries:main', children=[
            item('Категории', 'dictionaries:categories-list', in_menu=False, in_sitetree=True, children=[
                item('Добавить', 'dictionaries:categories-add'),
                item('{{ category }}',
                     'dictionaries:categories-detail category.slug',
                     in_menu=False,
                     in_sitetree=False,
                     children=[
                         item(
                             'Редактировать',
                             'dictionaries:categories-edit category.slug',
                             in_menu=False,
                             in_sitetree=False
                         ),
                         item(
                             'Удалить',
                             'dictionaries:categories-delete category.slug',
                             in_menu=False,
                             in_sitetree=False
                         ),

                         item('Типы справочников', 'dictionaries:types-list category.slug', in_menu=True,
                              in_sitetree=True,
                              children=[
                                  item('Добавить', 'dictionaries:types-add category.slug', in_menu=False,
                                       in_sitetree=False),
                                  item('{{ type.name }}', 'dictionaries:types-detail category.slug type.slug',
                                       in_menu=False, in_sitetree=False,
                                       children=[
                                           item('Редактировать', 'dictionaries:types-edit category.slug type.slug',
                                                in_menu=False, in_sitetree=False),
                                           item('Удалить', 'dictionaries:types-delete category.slug type.slug',
                                                in_menu=False, in_sitetree=False),

                                           item('Записи',
                                                'dictionaries:items-list category.slug type.slug',
                                                in_menu=False, in_sitetree=False, children=[
                                                   item('Добавить', 'dictionaries:items-add category.slug type.slug',
                                                        in_menu=False,
                                                        in_sitetree=False),
                                                   item('{{ dict_item.name }}',
                                                        'dictionaries:items-detail '
                                                        'category.slug type.slug dict_item.id',
                                                        in_menu=False, in_sitetree=False,
                                                        children=[
                                                            item(
                                                                'Редактировать',
                                                                'dictionaries:items-edit '
                                                                'category.slug type.slug dict_item.id',
                                                                in_menu=False,
                                                                in_sitetree=False
                                                            ),
                                                            item(
                                                                'Удалить',
                                                                'dictionaries:items-delete '
                                                                'category.slug type.slug dict_item.id',
                                                                in_menu=False,
                                                                in_sitetree=False
                                                            ),
                                                        ])
                                               ]),
                                       ])
                              ]),
                     ]),
            ]),
        ]),
    ]),
)


# item('Сформировать отчет', '', in_menu=True, in_sitetree=True),
# item('Загрузить данные', '', in_menu=True, in_sitetree=True),
# item('Фильтр', 'children:filter', in_menu=False, in_sitetree=False),
