from django.db import models
from common.models import NameUniqueModel, NameSlugUniqueModel


class Category(NameSlugUniqueModel):
    pass

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if self.position == 0:
            self.position = Category.objects.all().count() + 1
        return super().save(*args, **kwargs)


class DictionariesType(NameSlugUniqueModel):
    category = models.ForeignKey(Category, verbose_name='Категория')

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип справочника'
        verbose_name_plural = 'Типы справочников'

    def save(self, *args, **kwargs):
        if self.position == 0:
            self.position = DictionariesType.objects.filter(category=self.category).count() + 1
        return super().save(*args, **kwargs)


class Dictionary(NameUniqueModel):
    INSTITUTION_TYPE_CHOICE = (
        (0, 'Дошкольное'),
        (1, 'Школьное'),)

    type = models.ForeignKey(DictionariesType, verbose_name='Тип')
    institution_type = models.IntegerField('Тип учреждения', blank=True, null=True,
                                           choices=INSTITUTION_TYPE_CHOICE)

    class Meta:
        db_table = 'dictionaries'
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'
