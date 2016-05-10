from django.db import models
from django.db.models import permalink

from children.models import Child
from common.models import HistoryModel, NameModel
from parameters.base_models import HistoryParamsBase
from parameters.reference_models import GuideFamilyStatus, Institution, Group, Grade


class StudentHistory(HistoryParamsBase):
    institution = models.ForeignKey(Institution, verbose_name='Учреждение')
    group = models.ForeignKey(Group, verbose_name='Группа',
                              blank=True, null=True)
    grade = models.ForeignKey(Grade, verbose_name='Класс',
                              blank=True, null=True)

    class Meta:
        db_table = 'students'
        verbose_name = 'Истории обучения'
        verbose_name_plural = 'История обучения'

    def __str__(self):
        if self.last_date:
            return 'c {} по {}'.format(self.first_date, self.last_date)
        else:
            return 'c {} по н.в.'.format(self.first_date)

    @permalink
    def get_absolute_url(self):
        return 'educations:detail', None, {'child_id': self.child.id, 'education_id': self.id}


class FamilyStatusHistory(HistoryParamsBase):
    status = models.ManyToManyField(GuideFamilyStatus)

    class Meta:
        db_table = 'family_status'
        verbose_name = 'Истории статусов семей'
        verbose_name_plural = 'История статуса семьи'

    def __str__(self):
        status_list = []
        for status in self.status.all():
            status_list.append(status.get_status_display())
        return '{} {}'.format(self.child, status_list)


class HealthHistory(HistoryParamsBase):
    text = models.CharField('Сосотяние', max_length=128)

    class Meta:
        db_table = 'healths'
        verbose_name = 'Истории состояния здоровья'
        verbose_name_plural = 'История состояния здоровья'

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
        verbose_name = 'Истории примечаний'
        verbose_name_plural = 'История примечаний'

    def __str__(self):
        return '{} ({})'.format(self.child, self.text)
