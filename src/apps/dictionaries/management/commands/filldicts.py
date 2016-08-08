#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from src.settings import ROOT_DIR
from django.db import IntegrityError

from django.core.management import BaseCommand

from dictionaries.models import Category, DictionariesType, Dictionary


class DbFiller:
    def __init__(self, options):
        self.options = options

    def _clean_db(self):
        Category.objects.all().delete()
        DictionariesType.objects.all().delete()
        Dictionary.objects.all().delete()
        print('Database cleaned')

    def run(self):
        if self.options.get('clean', False):
            self._clean_db()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--clean',
                            action='store_true',
                            dest='clean',
                            default=False,
                            help='очистить данные всех справочников')

    def handle(self, *args, **options):
        runner = DbFiller(options=options)
        runner.run()
