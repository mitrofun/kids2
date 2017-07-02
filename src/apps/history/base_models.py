# -*- coding: utf-8 -*-
from django.db import models

from children.models import Child
from common.models import HistoryModel


class HistoryParamsBase(HistoryModel):
    child = models.ForeignKey(Child, verbose_name='Ребенок')

    class Meta:
        abstract = True
