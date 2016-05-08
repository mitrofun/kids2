from django.db import models

from common.models import HistoryModel
from educations.models import Institution, Grade, Group
from children.models import Child


class HistoryParamsBase(HistoryModel):
    child = models.ForeignKey(Child, verbose_name='Ребенок')

    class Meta:
        abstract = True


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
        verbose_name = 'Справочник статуса семьи'
        verbose_name_plural = 'Справочник статуса семьи'

    def __str__(self):
        return self.get_status_display()


class HealthHistory(HistoryParamsBase):
    text = models.CharField('Сосотяние', max_length=128)

    class Meta:
        db_table = 'healths'
        verbose_name = 'Здоровье'
        verbose_name_plural = 'Здоровье'

    def __str__(self):
        return '{} ({})'.format(self.child, self.text)


class RiskHistory(HistoryParamsBase):
    BOOL_CHOICES = (
        (True, 'Да'),
        (False, 'Нет')
        )
    group = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Группа риска')

    class Meta:
        db_table = 'risks'
        verbose_name = 'Группа риска'
        verbose_name_plural = 'Группа риска'

    def __str__(self):
        return '{} ({})'.format(self.child, self.get_group_display())


class NoteHistory(HistoryParamsBase):
    text = models.CharField('Сосотяние', max_length=256)

    class Meta:
        db_table = 'notes'
        verbose_name = 'Примечание'
        verbose_name_plural = 'Примечания'

    def __str__(self):
        return '{} ({})'.format(self.child, self.text)


class FamilyStatusHistory(HistoryParamsBase):
    status = models.ManyToManyField(GuideFamilyStatus)

    class Meta:
        db_table = 'family_status'
        verbose_name = 'Статус семьи'
        verbose_name_plural = 'Статусы семьи'

    def __str__(self):
        status_list = []
        for status in self.status.all():
            status_list.append(status.get_status_display())
        return '{} {}'.format(self.child, status_list)


class StudentHistory(HistoryParamsBase):
    institution = models.ForeignKey(Institution, verbose_name='Учреждение')
    group = models.ForeignKey(Group, verbose_name='Группа',
                              blank=True, null=True)
    grade = models.ForeignKey(Grade, verbose_name='Класс',
                              blank=True, null=True)

    class Meta:
        db_table = 'students'
        verbose_name = 'Учащийся'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return '{} ({})'.format(self.child, self.institution)
