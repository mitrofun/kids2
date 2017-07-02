from django.contrib import admin
from django import forms
from .models import Step
from dictionaries.models import Dictionary


class StepForm(forms.ModelForm):
    added_steps = Step.objects.all().values_list('level_id', flat=True)

    level = forms.ModelChoiceField(
        Dictionary.objects.filter(type__slug__in=['groups', 'grades']).exclude(id__in=added_steps),
        label='Уровень')

    class Meta:
        fields = ['level', 'position', ]
        model = Step


class StepAdmin(admin.ModelAdmin):
    form = StepForm

    list_display = ('level', 'position')


admin.site.register(Step, StepAdmin)
