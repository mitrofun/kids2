#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from common.models import NameModel


class GuideFamilyStatus(models.Model):

    FAMILY_STATUS = (
        (1, 'Многодетные'),
        (2, 'Малоимущие'),
        (3, 'Неполные'),
        (4, 'КМНС'),
        )
    status = models.IntegerField(blank=True, choices=FAMILY_STATUS)

    class Meta:
        db_table = 'guide_status'
        verbose_name = 'Статус семьи (Справочник)'
        verbose_name_plural = ' Статус семьи (Справочник)'

    def __str__(self):
        return self.get_status_display()


class Institution(NameModel):

    INSTITUTION_TYPE_CHOICE = (
        (0, 'Дошкольное'),
        (1, 'Школьное'),)

    type = models.IntegerField('Тип учреждения', blank=True, null=True,
                               choices=INSTITUTION_TYPE_CHOICE)

    class Meta:
        db_table = 'institutions'
        verbose_name = 'Учреждение (Справочник)'
        verbose_name_plural = ' Учреждения (Справочник)'


class Group(NameModel):
    pass

    class Meta:
        db_table = 'groups'
        verbose_name = 'Возрастная группа (Справочник)'
        verbose_name_plural = ' Возрастные группы (Справочник)'


class Grade(NameModel):
    pass

    class Meta:
        db_table = 'grades'
        verbose_name = 'Класс обучения (Справочник)'
        verbose_name_plural = ' Классы обучения (Справочник)'
