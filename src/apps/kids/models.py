from common.models import PersonModel, AddressModel


class Kid(PersonModel, AddressModel):
    pass

    class Meta:
        db_table = 'kids'
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

