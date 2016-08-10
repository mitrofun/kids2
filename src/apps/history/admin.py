from django.contrib import admin

from history.models import Param, ParamHistory

admin.site.register(Param)
admin.site.register(ParamHistory)
