#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from src.settings import ROOT_DIR
from django.db import IntegrityError
from django.core.management import BaseCommand
from dictionaries.models import Category, DictionariesType, Dictionary
from history.models import Param


class DbFiller:
    def __init__(self, options):
        self.options = options
        self._dic_name = None
        self._type = None

    def _fill_category(self):
        category_text = open(os.path.join(ROOT_DIR, "fixtures", "category.json"),
                             "r", encoding='utf-8').read()
        categories = json.loads(category_text)

        for category in categories:
            try:
                Category.objects.create(
                    pk=category["id"],
                    name=category["name"],
                    slug=category["slug"],
                    position=category["position"]
                )
            except IntegrityError as e:
                print('Error: {0} - {1}'.format(e, category["name"]))
        print('all category completed')

    def _fill_dictionary_by_name(self):
        dic_text = open(
            os.path.join(ROOT_DIR, "fixtures", "{}.json".format(self._dic_name)),
            "r", encoding='utf-8').read()
        dic = json.loads(dic_text)

        for item in dic:
            try:
                if self._dic_name == 'institutions':
                    Dictionary.objects.create(
                        name=item["name"],
                        institution_type=item["type"],
                        type_id=self._type
                    )
                else:
                    Dictionary.objects.create(
                        name=item["name"],
                        type_id=self._type
                    )
            except IntegrityError as e:
                print('Error: {0} - {1}'.format(e, item["name"]))
        print('{} completed'.format(self._dic_name))

    def _fill_all_dict(self):
        types_text = open(os.path.join(ROOT_DIR, "fixtures", "types.json"),
                          "r", encoding='utf-8').read()
        types = json.loads(types_text)

        for type in types:
            try:
                create_type = DictionariesType.objects.create(
                    name=type["name"],
                    slug=type["slug"],
                    position=type["position"],
                    category_id=type["category_id"]
                )

                self._dic_name = type["slug"]
                self._type = create_type.id
                print(self._dic_name)
                self._fill_dictionary_by_name()

            except IntegrityError as e:
                print('Error: {0} - {1}'.format(e, type["name"]))
        print('all types completed')

    def _fill_params(self):
        param_text = open(os.path.join(ROOT_DIR, "fixtures", "params.json"),
                          "r", encoding='utf-8').read()
        params = json.loads(param_text)

        for param in params:
            try:
                Param.objects.create(
                    name=param["name"],
                    slug=param["slug"],
                    position=param["position"]
                )
            except IntegrityError as e:
                print('Error: {0} - {1}'.format(e, param["name"]))
        print('all param completed')

    def _clean_db(self):
        Category.objects.all().delete()
        DictionariesType.objects.all().delete()
        Dictionary.objects.all().delete()
        Param.objects.all().delete()
        print('Database cleaned')

    def _fill_dictionaries(self):
        print('start fill dictionaries')
        self._fill_category()
        self._fill_all_dict()
        self._fill_params()

    def run(self):
        if self.options.get('clean', False):
            self._clean_db()
        if self.options.get('fill_dictionaries', False):
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
                            dest='fill_dictionaries',
                            default=False,
                            help='fill all dictionaries')

    def handle(self, *args, **options):
        runner = DbFiller(options=options)
        runner.run()
