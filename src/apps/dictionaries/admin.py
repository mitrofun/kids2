from django.contrib import admin
from dictionaries.models import GuideFamilyStatus, Institution, Group, Grade, Locality, Street


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)

admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Grade)
admin.site.register(Group)

admin.site.register(Locality)
admin.site.register(Street)

admin.site.register(GuideFamilyStatus)