from django.contrib import admin
from parameters.models import NoteHistory, HealthHistory, RiskHistory, \
    ParentsStatesHistory, StudentHistory


admin.site.register(StudentHistory)
admin.site.register(HealthHistory)


admin.site.register(ParentsStatesHistory)
admin.site.register(RiskHistory)
admin.site.register(NoteHistory)





