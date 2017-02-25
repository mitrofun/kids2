from django.db import models

from dictionaries.models import Dictionary


class Step(models.Model):
    level = models.ForeignKey(Dictionary, unique=True, verbose_name='Уровень')
    position = models.IntegerField(verbose_name='Номер', default=0)

    class Meta:
        db_table = 'steps'
        ordering = ['position']
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'

    def __str__(self):
        return '{} [{}]'.format(self.level.name, self.position)

    def save(self, *args, **kwargs):
        if self.position == 0:
            self.position = Step.objects.count() + 1
        return super(Step, self).save(*args, **kwargs)

    def get_next_position(self):
        try:
            next_position = self.position + 1
        except Step.DoesNotExist:
            next_position = 0
        return next_position

