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
                    item('Удалить', 'children:edit child.id', in_menu=False, in_sitetree=False),

                    item('История обучения', 'educations:list child.id', in_menu=False,
                         in_sitetree=False, children=[
                            item('Добавить', 'educations:add child.id', in_menu=False,
                                 in_sitetree=False),
                            item('{{ education }}', 'educations:detail child.id education.id',
                                 in_menu=False, in_sitetree=False, children=[
                                    item('Редактировать', 'educations:edit child.id education.id', in_menu=False,
                                         in_sitetree=False),
                                    item('Удалить', 'educations:edit child.id education.id', in_menu=False,
                                         in_sitetree=False),
                                    ]),
                            ]),
                    item('История здоровья', 'health:list child.id', in_menu=False,
                         in_sitetree=False, children=[
                            # item('Добавить', 'health:add child.id', in_menu=False,
                            #      in_sitetree=False),
                            # item('{{ health }}', 'health:detail child.id health.id',
                            #      in_menu=False, in_sitetree=False, children=[
                            #         item('Редактировать', 'health:edit child.id health.id', in_menu=False,
                            #              in_sitetree=False),
                            #         item('Удалить', 'health:edit child.id health.id', in_menu=False,
                            #              in_sitetree=False),
                            #     ]),
                        ]),
                ]),

        ]),
    ]),
)
