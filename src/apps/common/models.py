from django.db import models
from datetime import datetime
from children.functions import get_age


class CreatedModel(models.Model):
    created = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        abstract = True


class CreatedAndUpdatedModel(CreatedModel):
    updated = models.DateTimeField('Обновлен', auto_now=True)

    class Meta:
        abstract = True


class NameModel(models.Model):
    name = models.CharField('Наименование', max_length=128)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class NameUniqueModel(models.Model):
    name = models.CharField('Наименование', max_length=128, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class NameSlugUniqueModel(NameUniqueModel):
    slug = models.SlugField(verbose_name='Слаг', unique=True)
    position = models.IntegerField(verbose_name='Очередность', default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class HistoryModel(models.Model):
    first_date = models.DateField('Начальная дата', default=datetime.now)
    last_date = models.DateField('Конечная дата', blank=True, null=True)

    class Meta:
        abstract = True


class PersonModel(CreatedAndUpdatedModel):

    last_name = models.CharField('Фамилия', max_length=32)
    first_name = models.CharField('Имя', max_length=32)
    middle_name = models.CharField('Отчество', max_length=32, blank=True,
                                   null=True)
    birthday = models.DateField('Дата рождения', default=datetime.now)

    class Meta:
        abstract = True

    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name or '',
                                 self.middle_name or '')

    def get_short_name(self):
        return '{} {}.{}.'.format(self.last_name, self.first_name[:1] or '',
                                  self.middle_name[:1] or '')

    def get_age(self, date=datetime.now()):
        return get_age(self.birthday, date)

    def __str__(self):
        return self.get_full_name()


class AddressModel(models.Model):
    house = models.CharField('Дом', max_length=4, blank=True, null=True)
    flat = models.CharField('Квартира', max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
