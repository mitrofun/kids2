#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from children.functions import get_age
from datetime import date


class CalculateAge(TestCase):

    def test_get_age(self):
        # 0 year 0 month 0 day
        self.assertEqual(get_age(date(2010, 1, 1), date(2010, 1, 1)), 0)
        # 0 year 0 month 1 day
        self.assertEqual(get_age(date(2010, 1, 1), date(2010, 1, 2)), 0)
        # 0 year 11 month 30 day
        self.assertEqual(get_age(date(2010, 1, 1), date(2010, 12, 31)), 0)
        # 1 year 0 month 0 day
        self.assertEqual(get_age(date(2010, 1, 1), date(2011, 1, 1)), 1)
        # 6 year 5 month 29 day
        self.assertEqual(get_age(date(2010, 1, 1), date(2016, 6, 30)), 6)
        # 6 year 6 month 0 day
        self.assertEqual(get_age(date(2010, 1, 29), date(2016, 7, 29)), 6.6)
        self.assertEqual(get_age(date(2009, 12, 3), date(2016, 6, 3)), 6.6)
        self.assertEqual(get_age(date(2009, 6, 4), date(2016, 6, 3)), 6.6)
        # 6 year 6 month 1 day
        self.assertEqual(get_age(date(2010, 1, 29), date(2016, 7, 30)), 6.6)
        # 6 year 7 month 1 day
        self.assertEqual(get_age(date(2010, 1, 29), date(2016, 8, 30)), 6.6)
        # 7 year 0 month 0 day
        self.assertEqual(get_age(date(2010, 1, 29), date(2017, 1, 29)), 7)

