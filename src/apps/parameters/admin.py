from django.contrib import admin
from parameters.models import Institution, Group, Grade
from parameters.models import NoteHistory, HealthHistory, RiskHistory, \
    FamilyStatusHistory, StudentHistory
from parameters.reference_models import Locality, Street
from parameters.reference_models import GuideFamilyStatus


admin.site.register(Institution)
admin.site.register(Grade)
admin.site.register(Group)

admin.site.register(Locality)
admin.site.register(Street)

admin.site.register(StudentHistory)
admin.site.register(HealthHistory)

admin.site.register(GuideFamilyStatus)
admin.site.register(FamilyStatusHistory)
admin.site.register(RiskHistory)
admin.site.register(NoteHistory)





