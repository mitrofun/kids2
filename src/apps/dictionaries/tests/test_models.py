#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase

from dictionaries.models import Institution
from dictionaries.models import Grade, Group, Locality, Street, HealthStates, ParentsStatus


class InstitutionTest(TestCase):

    def setUp(self):
        self.institutions_before_school = Institution.objects.create(name='Дошкольная организация', type=0)
        self.institutions_school = Institution.objects.create(name='Общееобразовательная организация', type=1)

    def test_filter(self):
        institutions_before_school = Institution.objects.filter(type=0)
        institutions_school = Institution.objects.filter(type=1)
        self.assertEqual(institutions_before_school.count(), 1)
        self.assertEqual(institutions_school.count(), 1)

    def test_urls(self):
        self.assertEqual(self.institutions_school.get_absolute_url(), '/dictionaries/education/institutions/2/')


class ElementaryTest(TestCase):
    def setUp(self):
        self.education_url = '/dictionaries/education/'
        self.address_url = '/dictionaries/address/'
        self.secondary_url = '/dictionaries/secondary/'

        self.grade = Grade.objects.create(name='1 класс')
        self.group = Group.objects.create(name='Младшая')
        self.locality = Locality.objects.create(name='Москва')
        self.street = Street.objects.create(name='Мира')
        self.health_states = HealthStates.objects.create(name='Здоровый')
        self.parents_status = ParentsStatus.objects.create(name='Отличная')

    def test_urls(self):

        self.assertEqual(self.grade.get_absolute_url(), self.education_url + 'grades/1/')
        self.assertEqual(self.grade.get_edit_url(), self.education_url + 'grades/1/edit/')
        self.assertEqual(self.grade.get_delete_url(), self.education_url + 'grades/1/delete/')

        self.assertEqual(self.group.get_absolute_url(), self.education_url + 'groups/1/')
        self.assertEqual(self.group.get_edit_url(), self.education_url + 'groups/1/edit/')
        self.assertEqual(self.group.get_delete_url(), self.education_url + 'groups/1/delete/')

        self.assertEqual(self.locality.get_absolute_url(), self.address_url + 'locality/1/')
        self.assertEqual(self.locality.get_edit_url(), self.address_url + 'locality/1/edit/')
        self.assertEqual(self.locality.get_delete_url(), self.address_url + 'locality/1/delete/')

        self.assertEqual(self.street.get_absolute_url(), self.address_url + 'streets/1/')
        self.assertEqual(self.street.get_edit_url(), self.address_url + 'streets/1/edit/')
        self.assertEqual(self.street.get_delete_url(), self.address_url + 'streets/1/delete/')

        self.assertEqual(self.health_states.get_absolute_url(), self.secondary_url + 'health/1/')
        self.assertEqual(self.health_states.get_edit_url(), self.secondary_url + 'health/1/edit/')
        self.assertEqual(self.health_states.get_delete_url(), self.secondary_url + 'health/1/delete/')

        self.assertEqual(self.parents_status.get_absolute_url(), self.secondary_url + 'parents/1/')
        self.assertEqual(self.parents_status.get_edit_url(), self.secondary_url + 'parents/1/edit/')
        self.assertEqual(self.parents_status.get_delete_url(), self.secondary_url + 'parents/1/delete/')
