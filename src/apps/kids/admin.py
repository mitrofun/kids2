from django.contrib import admin
from kids.models import Kid
from reversion.admin import VersionAdmin


class ModelAdmin(VersionAdmin):
    pass


admin.site.register(Kid, ModelAdmin)
