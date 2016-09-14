from django.db.models import permalink
from django.db import models
from common.models import PersonModel, AddressModel
from dictionaries.models import Dictionary


class Child(PersonModel, AddressModel):
    locality = models.ForeignKey(Dictionary, verbose_name="Населенный пункт",
                                 related_name='locality', blank=True, null=True)
    street = models.ForeignKey(Dictionary, verbose_name="Улица", related_name='street', blank=True, null=True)

    class Meta:
        db_table = 'children'
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

    @permalink
    def get_absolute_url(self):
        return 'children:detail', None, {'child_id': self.id}
