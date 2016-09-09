from django.db import models
from children.models import Child
from common.models import HistoryModel, NameSlugUniqueModel
from history.base_models import HistoryParamsBase
from dictionaries.models import Category, DictionariesType, Dictionary
from datetime import timedelta


class Param(NameSlugUniqueModel):
    pass

    class Meta:
        db_table = 'param'
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'
        ordering = ['position', ]

    def save(self, *args, **kwargs):
        if self.position == 0:
            self.position = Param.objects.all().count() + 1
        return super().save(*args, **kwargs)


class ParamHistory(HistoryParamsBase):

    BOOL_CHOICES = (
        (True, 'Да'),
        (False, 'Нет')
    )

    parameter = models.ForeignKey(Param, verbose_name='Параметр')
    institution = models.ForeignKey(Dictionary, verbose_name='Учреждение',
                                    related_name="history_institution", blank=True, null=True)
    group = models.ForeignKey(Dictionary, verbose_name='Группа',
                              related_name="history_group", blank=True, null=True)
    grade = models.ForeignKey(Dictionary, verbose_name='Класс',
                              related_name="history_grade", blank=True, null=True)
    parents_status = models.ManyToManyField(Dictionary, verbose_name='Статус семьи',
                                            related_name="history_parents_status", blank=True)
    health_states = models.ManyToManyField(Dictionary, verbose_name='Состояние здоровья',
                                           related_name="history_health_states", blank=True)
    risk_group = models.BooleanField(choices=BOOL_CHOICES, verbose_name='Группа риска')
    note = models.CharField('Примечание', max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'param_history'
        verbose_name = 'Истории параметров'
        verbose_name_plural = 'История параметров'
        ordering = ['-first_date', '-last_date', ]

    def __str__(self):
        if self.last_date:
            return 'c {} по {} - {}'.format(self.first_date, self.last_date, self.parameter.name)
        else:
            return 'c {} по н.в. - {}'.format(self.first_date, self.parameter.name)

    def save(self, *args, **kwargs):

        one_day = timedelta(days=1)

        all_history_list = ParamHistory.objects.filter(child=self.child).\
            filter(parameter__slug=self.parameter.slug).order_by('first_date')

        open_history_list = all_history_list.filter(last_date=None)

        if len(open_history_list):
            for open_history in open_history_list:
                if open_history.first_date <= self.first_date - one_day:
                    open_history.last_date = self.first_date - one_day
                    open_history.save()

        return super(ParamHistory, self).save(*args, **kwargs)
