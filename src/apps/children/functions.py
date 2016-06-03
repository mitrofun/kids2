#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date


def get_age(birthday, on_date=date.today()):
    """
    Функция получения возраста ребенка в годах на дату,
    если дата не указана берем на текущий день

    :param birthday: День рождения ребенка(дата)
    :param on_date: Дата, по умолчанию сегодня
    :return: Возраст ребенка от 0 до 6 ,отдельно 6.6 , 7 и далее
    """

    age = on_date.year - birthday.year
    if on_date.month < birthday.month:
        age -= 1
    elif on_date.month == birthday.month and on_date.day < birthday.day:
        age -= 1
        month = birthday.month
        days = on_date.day - birthday.day
        if age == 6:
            if month == 6 and abs(days) >= 1:
                age = 6.6
    if age == 6:
        delta_month = abs(on_date.month - birthday.month)
        if delta_month == 6:
            delta_day = abs(on_date.day - birthday.day)
            if delta_day >= 0:
                age = 6.6
        if delta_month > 6:
            age = 6.6
    return age
