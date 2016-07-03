from django.db import models
from django.db.models import permalink

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
        verbose_name = 'Статус семьи'
        verbose_name_plural = ' Статус семьи'

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
        verbose_name = 'Учреждение'
        verbose_name_plural = ' Учреждения'

    @permalink
    def get_absolute_url(self):
        return 'institutions:detail', None, {'institution_id': self.id}


class Group(NameModel):
    pass

    class Meta:
        db_table = 'groups'
        verbose_name = 'Возрастная группа'
        verbose_name_plural = ' Возрастные группы'


class Grade(NameModel):
    pass

    class Meta:
        db_table = 'grades'
        verbose_name = 'Класс обучения'
        verbose_name_plural = ' Классы обучения'


class Locality(NameModel):
    pass

    class Meta:
        db_table = 'locality'
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'


class Street(NameModel):
    pass

    class Meta:
        db_table = 'streets'
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
