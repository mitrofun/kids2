#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sitetree.utils import tree, item

sitetrees = (
    tree('dictionaries', items=[
        item('Справочники', 'dictionaries:main', children=[
            item('Категории', 'dictionaries:categories-list', in_menu=False, in_sitetree=True, children=[
                item('Добавить', 'dictionaries:categories-add'),
                item('{{ category }}', 'dictionaries:categories-detail category.slug', in_menu=False, in_sitetree=False,
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

                                           item('Записи в справочнике "{{ type }}"',
                                                'dictionaries:items-list category.slug type.slug',
                                                in_menu=False, in_sitetree=False, children=[
                                                   item('Добавить', 'dictionaries:items-add category.slug type.slug',
                                                        in_menu=False,
                                                        in_sitetree=False),
                                                   item('{{ item.name }}',
                                                        'dictionaries:items-detail category.slug type.slug item.id',
                                                        in_menu=False, in_sitetree=False,
                                                        children=[

                                                        ])
                                               ]),
                                       ])
                              ]),
                     ]),

            ]),

        ]),
    ]),
)


#
# sitetrees = (
#     tree('dictionaries_tree', items=[
#
#         item('Справочники', 'dictionaries', children=[
#             item('Образование', 'education', in_menu=True, in_sitetree=True,  children=[
#                 item('Учреждения', 'institutions:list', in_menu=True, in_sitetree=True,  children=[
#                     item('Добавить', 'institutions:add', in_menu=False, in_sitetree=False),
#                     item('{{ obj.name }}', 'institutions:detail obj.id', in_menu=True,
#                          in_sitetree=True, children=[
#                             item('Редактировать', 'institutions:edit obj.id', in_menu=False, in_sitetree=False),
#                             item('Удалить', 'institutions:delete obj.id', in_menu=False, in_sitetree=False),
#                     ])
#                 ]),
#                 item('Возрастные группы', 'groups:list', in_menu=True, in_sitetree=True,  children=[
#                     item('Добавить', 'groups:add', in_menu=False, in_sitetree=False),
#                     item('{{ obj.name }}', 'groups:detail obj.id', in_menu=False, in_sitetree=False, children=[
#                         item('Редактировать', 'groups:edit obj.id', in_menu=False, in_sitetree=False),
#                         item('Удалить', 'groups:delete obj.id', in_menu=False, in_sitetree=False),
#                     ])
#                 ]),
#                 item('Классы', 'grades:list', in_menu=True, in_sitetree=True,  children=[
#                     item('Добавить', 'grades:add', in_menu=False, in_sitetree=False),
#                     item('{{ obj.name }}', 'grades:detail obj.id', in_menu=False, in_sitetree=False, children=[
#                         item('Редактировать', 'grades:edit obj.id', in_menu=False, in_sitetree=False),
#                         item('Удалить', 'grades:delete obj.id', in_menu=False, in_sitetree=False),
#                     ])
#                 ])
#             ]),
#             item('Адреса', 'address', in_menu=True, in_sitetree=True, children=[
#                 item('Населенные пункты', 'locality:list', in_menu=True, in_sitetree=True, children=[
#                     item('Добавить', 'obj:add', in_menu=False, in_sitetree=False),
#                     item('{{ obj.name }}', 'locality:detail obj.id', in_menu=False, in_sitetree=False, children=[
#                         item('Редактировать', 'locality:edit obj.id', in_menu=False, in_sitetree=False),
#                         item('Удалить', 'locality:delete obj.id', in_menu=False, in_sitetree=False),
#                     ])
#                 ]),
#                 item('Улицы', 'streets:list', in_menu=True, in_sitetree=True, children=[
#                     item('Добавить', 'streets:add', in_menu=False, in_sitetree=False),
#                     item('{{ obj.name }}', 'streets:detail obj.id', in_menu=False, in_sitetree=False, children=[
#                         item('Редактировать', 'streets:edit obj.id', in_menu=False, in_sitetree=False),
#                         item('Удалить', 'streets:delete obj.id', in_menu=False, in_sitetree=False),
#                     ])
#                 ]),
#             ]),
#             item('Дополнительные', 'secondary', in_menu=True, in_sitetree=True, children=[
#                 item('Состояния здоровья', 'health:list', in_menu=True, in_sitetree=True, children=[
#                     item('Добавить', 'health:add', in_menu=False, in_sitetree=False),
#                     item('{{ obj.name }}', 'health:detail obj.id', in_menu=False, in_sitetree=False, children=[
#                         item('Редактировать', 'health:edit obj.id', in_menu=False, in_sitetree=False),
#                         item('Удалить', 'health:delete obj.id', in_menu=False, in_sitetree=False),
#                     ])
#                 ]),
#                 item('Статусы родителей', 'parents:list', in_menu=True, in_sitetree=True, children=[
#                     item('Добавить', 'parents:add', in_menu=False, in_sitetree=False),
#                     item('{{ obj.name }}', 'parents:detail obj.id', in_menu=False, in_sitetree=False, children=[
#                         item('Редактировать', 'parents:edit obj.id', in_menu=False, in_sitetree=False),
#                         item('Удалить', 'parents:delete obj.id', in_menu=False, in_sitetree=False),
#                     ])
#                 ]),
#             ]),
#         ]),
#         # item('Сформировать отчет', '', in_menu=True, in_sitetree=True),
#         # item('Загрузить данные', '', in_menu=True, in_sitetree=True),
#         # item('Фильтр', 'children:filter', in_menu=False, in_sitetree=False),
#     ]),
# )
