from django.contrib import admin
from parameters.models import NoteHistory, HealthHistory, RiskHistory, \
    FamilyStatusHistory, StudentHistory


admin.site.register(StudentHistory)
admin.site.register(HealthHistory)


admin.site.register(FamilyStatusHistory)
admin.site.register(RiskHistory)
admin.site.register(NoteHistory)





