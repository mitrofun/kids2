#!/usr/bin/env python
# -*- coding: utf-8 -*-
from children.models import Child
from django.db.models import Q
from django_filters import FilterSet, MethodFilter
import django.forms.widgets as widgets


class ChildrenFilter(FilterSet):
    date = MethodFilter(action="children_on_date", label='Дата',
                        widget=widgets.DateInput())

    class Meta:
        model = Child
        fields = ['date']

    def children_on_date(self, queryset, value):
        return queryset.filter(studenthistory__first_date__lte=value).\
            filter(Q(studenthistory__last_date__gt=value) |
                   Q(studenthistory__last_date__isnull=True))

