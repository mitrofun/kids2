from common.models import PersonModel, AddressModel


class Child(PersonModel, AddressModel):
    pass

    class Meta:
        db_table = 'children'
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

