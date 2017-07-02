# -*- coding: utf-8 -*-
from datetime import date

from src.apps.children.functions import get_age


def test_get_age():
    # 0 year 0 month 0 day
    assert get_age(date(2010, 1, 1), date(2010, 1, 1)) == 0
    # 0 year 0 month 1 day
    assert get_age(date(2010, 1, 1), date(2010, 1, 2)) == 0
    # 0 year 11 month 30 day
    assert get_age(date(2010, 1, 1), date(2010, 12, 31)) == 0
    # 1 year 0 month 0 day
    assert get_age(date(2010, 1, 1), date(2011, 1, 1)) == 1
    # 6 year 5 month 29 day
    assert get_age(date(2010, 1, 1), date(2016, 6, 30)) == 6
    # 6 year 6 month 0 day
    assert get_age(date(2010, 1, 29), date(2016, 7, 29)) == 6.6
    assert get_age(date(2009, 12, 3), date(2016, 6, 3)) == 6.6
    assert get_age(date(2009, 6, 4), date(2016, 6, 3)) == 6.6
    assert get_age(date(2010, 1, 5), date(2016, 7, 5)) == 6.6
    # 6 year 6 month 1 day
    assert get_age(date(2010, 1, 29), date(2016, 7, 30)) == 6.6
    # 6 year 7 month 1 day
    assert get_age(date(2010, 1, 29), date(2016, 8, 30)) == 6.6
    # 7 year 0 month 0 day
    assert get_age(date(2010, 1, 29), date(2017, 1, 29)) == 7
