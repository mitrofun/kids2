# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 16:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('last_name', models.CharField(max_length=32, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=32, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='Отчество')),
                ('birthday', models.DateField(default=datetime.datetime(2016, 4, 4, 16, 59, 19, 895150), verbose_name='Дата рождения')),
                ('sex', models.IntegerField(blank=True, choices=[(0, 'жен'), (1, 'муж')], null=True, verbose_name='Пол')),
                ('locality', models.CharField(max_length=32, verbose_name='Населенный пункт')),
                ('street', models.CharField(max_length=32, verbose_name='Улица')),
                ('house', models.CharField(blank=True, max_length=4, null=True, verbose_name='Дом')),
                ('flat', models.CharField(blank=True, max_length=4, null=True, verbose_name='Квартира')),
            ],
            options={
                'verbose_name': 'Ребенок',
                'verbose_name_plural': 'Дети',
                'db_table': 'kids',
            },
        ),
    ]
