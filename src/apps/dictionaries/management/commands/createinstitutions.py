#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from src.settings import ROOT_DIR
from django.db import IntegrityError

from django.core.management import BaseCommand

from dictionaries.models import Institution


class DbFiller:
    def __init__(self, options):
        self.options = options
        self.institutions = None

    def run(self):
        if not self.options.get('clean', False):
            self.institutions = self._get_institutions()
            print('Added {} institutions'.format(len(self.institutions)))
        if self.options.get('clean', False):
            self._clean_db()

    def _clean_db(self):
        Institution.objects.all().delete()
        print('Database cleaned')

    def _get_institutions(self):
        institutions_text = open(os.path.join(ROOT_DIR, "fixtures", "institutions.json"), "r", encoding='utf-8').read()
        institutions = json.loads(institutions_text)
        for institution in institutions:
            try:
                Institution.objects.create(name=institution["name"], type=institution["type"])
            except IntegrityError as e:
                print('Error: {0} - {1}'.format(e, institution["name"]))
        return Institution.objects.all()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--clean',
                            action='store_true',
                            dest='clean',
                            default=False,
                            help='очистить предварительно базу')
        parser.add_argument('--create',
                            nargs='*',
                            default=True,
                            dest='institutions',
                            help='загрузка в справочник образовательных учреждений')

    def handle(self, *args, **options):
        runner = DbFiller(options=options)
        runner.run()
