#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from transfer.functions import run_transfer


class Command(BaseCommand):
    help = 'Transfer children '

    def handle(self, *args, **options):
        run_transfer()
