# -*- coding: utf-8 -*-
from sitetree.utils import tree, item

sitetrees = (
    tree('loader', items=[
        item('Загрузка данных', 'loader', in_menu=True, in_sitetree=True),
        ]),
)
