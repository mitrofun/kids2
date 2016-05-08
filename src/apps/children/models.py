from django.db.models import permalink

from common.models import PersonModel, AddressModel


class Child(PersonModel, AddressModel):
    pass

    class Meta:
        db_table = 'children'
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

    @permalink
    def get_absolute_url(self):
        return 'children:detail', None, {'child_id': self.id}
