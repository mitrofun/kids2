#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from django.core.management import BaseCommand

from dictionaries.models import Institution, Grade, Group
from dictionaries.models import Locality, Street
from dictionaries.models import ParentsStatus, HealthStates

INSTITUTIONS = {
    {"name": ""}
}