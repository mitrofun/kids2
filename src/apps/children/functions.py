#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date


def get_age(birthday, on_date=date.today()):

    age = on_date.year - birthday.year
    if on_date.month < birthday.month:
        age -= 1
    elif on_date.month == birthday.month and on_date.day < birthday.day:
        age -= 1
    return age
