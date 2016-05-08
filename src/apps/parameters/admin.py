from django.contrib import admin
from parameters.models import Institution, Group, Grade
from parameters.models import NoteHistory, HealthHistory, RiskHistory, \
    FamilyStatusHistory, StudentHistory
from parameters.secondary_models import GuideFamilyStatus


admin.site.register(Institution)
admin.site.register(Grade)
admin.site.register(Group)
admin.site.register(GuideFamilyStatus)


admin.site.register(StudentHistory)
admin.site.register(HealthHistory)
admin.site.register(FamilyStatusHistory)
admin.site.register(RiskHistory)
admin.site.register(NoteHistory)





