from django.db import models
from datetime import datetime


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


class PersonModel(CreatedAndUpdatedModel):

    SEX_CHOICE = (
        (0, 'жен'),
        (1, 'муж'),)

    last_name = models.CharField('Фамилия', max_length=32)
    first_name = models.CharField('Имя', max_length=32)
    middle_name = models.CharField('Отчество', max_length=32, blank=True,
                                   null=True)
    birthday = models.DateField('Дата рождения', default=datetime.now())
    sex = models.IntegerField('Пол', choices=SEX_CHOICE, blank=True, null=True)

    class Meta:
        abstract = True

    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name or '',
                                 self.middle_name or '')

    def get_short_name(self):
        return '{} {}.{}.'.format(self.last_name, self.first_name[:1] or '',
                                  self.middle_name[:1] or '')

    def get_age(self):
        return datetime.today().year - self.birthday.year

    def __str__(self):
        return self.get_full_name()


class AddressModel(models.Model):
    locality = models.CharField('Населенный пункт', max_length=32)
    street = models.CharField('Улица', max_length=32)
    house = models.CharField('Дом', max_length=4, blank=True, null=True)
    flat = models.CharField('Квартира', max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
