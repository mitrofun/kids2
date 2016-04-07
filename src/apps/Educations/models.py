from django.db import models

from common.models import NameModel


class Institution(NameModel):

    INSTITUTION_TYPE_CHOICE = (
        (0, 'Дошкольное'),
        (1, 'Школьное'),)

    type = models.IntegerField('Тип учреждения', blank=True, null=True,
                               choices=INSTITUTION_TYPE_CHOICE)

    class Meta:
        db_table = 'institutions'
        verbose_name = 'Учреждение'
        verbose_name_plural = 'Учреждения'


class Group(NameModel):
    pass

    class Meta:
        db_table = 'groups'
        verbose_name = 'Возрастная группа'
        verbose_name_plural = 'Возрастные группы'


class Grade(NameModel):
    pass

    class Meta:
        db_table = 'grades'
        verbose_name = 'Класс обучения'
        verbose_name_plural = 'Классы обучения'
