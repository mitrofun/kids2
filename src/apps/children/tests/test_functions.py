#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from children.functions import get_age
from datetime import date


class CalculateAge(TestCase):

    def test_get_age(self):
        self.assertEqual(get_age(date(2015, 1, 1)), 1)
