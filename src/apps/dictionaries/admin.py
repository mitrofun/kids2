from django.contrib import admin
from dictionaries.models import Category, DictionariesType, Dictionary


class DictionariesTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'position')
    list_filter = ('category',)


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)


admin.site.register(Category)
admin.site.register(DictionariesType, DictionariesTypeAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
