from django.db import models
from django.db.models import permalink
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

    @permalink
    def get_absolute_url(self):
        return 'dictionaries:categories-detail', None, {'category': self.slug}

    @permalink
    def get_edit_url(self):
        return 'dictionaries:categories-edit', None, {'category': self.slug}

    @permalink
    def get_delete_url(self):
        return 'dictionaries:categories-delete', None, {'category': self.slug}


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

    @permalink
    def get_absolute_url(self):
        return 'dictionaries:types-detail', None, {'category': self.category.slug, 'dictionary_type': self.slug}

    @permalink
    def get_edit_url(self):
        return 'dictionaries:types-edit', None, {'category': self.category.slug, 'dictionary_type': self.slug}

    @permalink
    def get_delete_url(self):
        return 'dictionaries:types-delete', None, {'category': self.category.slug, 'dictionary_type': self.slug}


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
