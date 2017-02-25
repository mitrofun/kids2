#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from django.db.models import Q

from history.models import ParamHistory


def run_transfer(on_date=datetime.now()):  # datetime(2017, 9, 1).date()

    history_qs = ParamHistory.objects.filter(Q(group_id__isnull=False) | Q(grade_id__isnull=False)).\
        filter(last_date__isnull=True)

    for history in history_qs:
        history.set_next_step(date=on_date)
