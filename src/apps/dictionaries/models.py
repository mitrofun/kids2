from django.db import models
from django.db.models import permalink

from common.models import NameUniqueModel

#
# class Institution(NameUniqueModel):
#
#     INSTITUTION_TYPE_CHOICE = (
#         (0, 'Дошкольное'),
#         (1, 'Школьное'),)
#
#     type = models.IntegerField('Тип учреждения', blank=True, null=True,
#                                choices=INSTITUTION_TYPE_CHOICE)
#
#     class Meta:
#         db_table = 'institutions'
#         verbose_name = 'Учреждение'
#         verbose_name_plural = ' Учреждения'
#
#     @permalink
#     def get_absolute_url(self):
#         return 'institutions:detail', None, {'institution_id': self.id}
#
#
# class ParentsStatus(NameUniqueModel):
#     pass
#
#     class Meta:
#         db_table = 'parents_status'
#         verbose_name = 'Статус родителей'
#         verbose_name_plural = ' Статусы родителей(семьи)'
#
#     @permalink
#     def get_absolute_url(self):
#         return 'parents:detail', None, {'parent_id': self.id}
#
#     @permalink
#     def get_edit_url(self):
#         return 'parents:edit', None, {'parent_id': self.id}
#
#     @permalink
#     def get_delete_url(self):
#         return 'parents:delete', None, {'parent_id': self.id}
#
#
# class HealthStates(NameUniqueModel):
#     pass
#
#     class Meta:
#         db_table = 'health_states'
#         verbose_name = 'Состояние здоровья'
#         verbose_name_plural = 'Состояния здоровья'
#
#     @permalink
#     def get_absolute_url(self):
#         return 'health:detail', None, {'health_id': self.id}
#
#     @permalink
#     def get_edit_url(self):
#         return 'health:edit', None, {'health_id': self.id}
#
#     @permalink
#     def get_delete_url(self):
#         return 'health:delete', None, {'health_id': self.id}
#
#
# class Group(NameUniqueModel):
#     pass
#
#     class Meta:
#         db_table = 'groups'
#         verbose_name = 'Возрастная группа'
#         verbose_name_plural = ' Возрастные группы'
#
#     @permalink
#     def get_absolute_url(self):
#         return 'groups:detail', None, {'group_id': self.id}
#
#     @permalink
#     def get_edit_url(self):
#         return 'groups:edit', None, {'group_id': self.id}
#
#     @permalink
#     def get_delete_url(self):
#         return 'groups:delete', None, {'group_id': self.id}
#
#
# class Grade(NameUniqueModel):
#     pass
#
#     class Meta:
#         db_table = 'grades'
#         verbose_name = 'Класс обучения'
#         verbose_name_plural = ' Классы обучения'
#
#     @permalink
#     def get_absolute_url(self):
#         return 'grades:detail', None, {'grade_id': self.id}
#
#     @permalink
#     def get_edit_url(self):
#         return 'grades:edit', None, {'grade_id': self.id}
#
#     @permalink
#     def get_delete_url(self):
#         return 'grades:delete', None, {'grade_id': self.id}
#
#
# class Locality(NameUniqueModel):
#     pass
#
#     class Meta:
#         db_table = 'locality'
#         verbose_name = 'Населенный пункт'
#         verbose_name_plural = 'Населенные пункты'
#
#     @permalink
#     def get_absolute_url(self):
#         return 'locality:detail', None, {'locality_id': self.id}
#
#     @permalink
#     def get_edit_url(self):
#         return 'locality:edit', None, {'locality_id': self.id}
#
#     @permalink
#     def get_delete_url(self):
#         return 'locality:delete', None, {'locality_id': self.id}
#
#
# class Street(NameUniqueModel):
#     pass
#
#     class Meta:
#         db_table = 'streets'
#         verbose_name = 'Улица'
#         verbose_name_plural = 'Улицы'
#
#     @permalink
#     def get_absolute_url(self):
#         return 'streets:detail', None, {'street_id': self.id}
#
#     @permalink
#     def get_edit_url(self):
#         return 'streets:edit', None, {'street_id': self.id}
#
#     @permalink
#     def get_delete_url(self):
#         return 'streets:delete', None, {'street_id': self.id}


class Handbook(NameUniqueModel):
    INSTITUTION_TYPE = 1
    GROUPS_TYPE = 2
    GRADES_TYPE = 3
    LOCALITY_TYPE = 4
    STREETS_TYPE = 5
    HEALTH_TYPE = 6
    PARENTS_TYPE = 7

    TYPE_CHOICES = (
        (INSTITUTION_TYPE, 'institutions'),
        (GROUPS_TYPE, 'groups'),
        (GRADES_TYPE, 'grades'),
        (LOCALITY_TYPE, 'locality'),
        (STREETS_TYPE, 'streets'),
        (HEALTH_TYPE, 'health'),
        (PARENTS_TYPE, 'parents'),
    )

    INSTITUTION_TYPE_CHOICE = (
        (0, 'Дошкольное'),
        (1, 'Школьное'),)

    dict_type = models.IntegerField(choices=TYPE_CHOICES, default=INSTITUTION_TYPE)
    type = models.IntegerField('Тип учреждения', blank=True, null=True, choices=INSTITUTION_TYPE_CHOICE)

    class Meta:
        db_table = 'handbooks'
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'
