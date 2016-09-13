#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from dictionaries.models import Dictionary, DictionariesType, Category
from common.utils import get_display_age, get_institution


class DisplayAgeString(TestCase):

    def test_get_age(self):
        self.assertEqual(get_display_age(10), '10 лет')
        self.assertEqual(get_display_age(1), '1 год')
        self.assertEqual(get_display_age(19), 'старше 18 лет')
        self.assertEqual(get_display_age(6.6), '6 лет 6м')
        self.assertEqual(get_display_age(100), 'старше 18 лет')
        self.assertEqual(get_display_age(0), 'проверте дату рождения')


class InstitutionList(TestCase):

    def setUp(self):
        category = Category.objects.create(name='Образование', slug='education')
        _type = DictionariesType.objects.create(category=category, slug='institutions', name='Учреждения')
        Dictionary.objects.create(type=_type, institution_type=0, name='Садик')
        Dictionary.objects.create(type=_type, institution_type=1, name='Школа')

    def test_institution_list(self):
        self.assertEqual(len(get_institution()), 2)
        self.assertEqual(len(get_institution(0)), 1)
        self.assertEqual(len(get_institution(1)), 1)
