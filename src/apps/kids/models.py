from common.models import PersonModel, AddressModel
from reversion import revisions as reversion


@reversion.register()
class Kid(PersonModel, AddressModel):
    pass

    class Meta:
        db_table = 'kids'
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'
