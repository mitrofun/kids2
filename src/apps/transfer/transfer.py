#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Q
from history.models import ParamHistory
from datetime import datetime


def run_transfer(on_date=datetime.now()):

    history_qs = ParamHistory.objects.filter(Q(group_id__isnull=False) | Q(grade_id__isnull=False))

    for history in history_qs:
        history.set_next_step(date=on_date)

