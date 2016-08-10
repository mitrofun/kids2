#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from src.settings import ROOT_DIR
from django.db import IntegrityError
from django.core.management import BaseCommand
from history.models import Param


class DbFiller:
    def __init__(self, options):
        self.options = options
        self._dic_name = None
        self._type = None

    def _fill_params(self):
        params_text = open(os.path.join(ROOT_DIR, "fixtures", "params.json"), "r", encoding='utf-8').read()
        params = json.loads(params_text)

        for param in params:
            try:
                Param.objects.create(
                    name=param["name"],
                    slug=param["slug"],
                    position=param["position"]
                )
            except IntegrityError as e:
                print('Error: {0} - {1}'.format(e, param["name"]))
        print('all params completed')

    def _clean_db(self):
        Param.objects.all().delete()
        print('Param cleaned')

    def _fill_dictionaries(self):
        print('start fill parameters')
        self._fill_params()

    def run(self):
        if self.options.get('clean', False):
            self._clean_db()
        if self.options.get('fill_params', False):
            self._fill_dictionaries()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--clean',
                            action='store_true',
                            dest='clean',
                            default=False,
                            help='clean all dictionaries')
        parser.add_argument('--fill',
                            action='store_true',
                            dest='fill_params',
                            default=False,
                            help='fill parameters')

    def handle(self, *args, **options):
        runner = DbFiller(options=options)
        runner.run()
