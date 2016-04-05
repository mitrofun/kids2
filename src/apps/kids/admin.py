from django.contrib import admin
from kids.models import Kid


class ModelAdmin(admin.ModelAdmin):
    list_display = \
        ('last_name', 'first_name', 'middle_name', 'birthday', 'get_age')
    list_display_links = ('first_name', 'last_name')
    list_filter = ('last_name', 'first_name', 'middle_name')


admin.site.register(Kid, ModelAdmin)
