from django.contrib import admin

from parameters.models import NoteHistory, HealthHistory, RiskHistory, \
    StudentHistory, FamilyStatusHistory, GuideFamilyStatus


admin.site.register(NoteHistory)
admin.site.register(HealthHistory)
admin.site.register(RiskHistory)
admin.site.register(StudentHistory)
admin.site.register(FamilyStatusHistory)
admin.site.register(GuideFamilyStatus)
