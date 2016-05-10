# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 11:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('children', '0002_remove_child_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyStatusHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_date', models.DateField(default=datetime.datetime.now, verbose_name='Начальная дата')),
                ('last_date', models.DateField(blank=True, null=True, verbose_name='Конечная дата')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children.Child', verbose_name='Ребенок')),
            ],
            options={
                'verbose_name_plural': 'История статуса семьи',
                'db_table': 'family_status',
                'verbose_name': 'Истории статусов семей',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': ' Классы обучения (Справочник)',
                'db_table': 'grades',
                'verbose_name': 'Класс обучения (Справочник)',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': ' Возрастные группы (Справочник)',
                'db_table': 'groups',
                'verbose_name': 'Возрастная группа (Справочник)',
            },
        ),
        migrations.CreateModel(
            name='GuideFamilyStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Многодетные'), (2, 'Малоимущие'), (3, 'Неполные'), (4, 'КМНС')])),
            ],
            options={
                'verbose_name_plural': ' Статус семьи (Справочник)',
                'db_table': 'guide_status',
                'verbose_name': 'Статус семьи (Справочник)',
            },
        ),
        migrations.CreateModel(
            name='HealthHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_date', models.DateField(default=datetime.datetime.now, verbose_name='Начальная дата')),
                ('last_date', models.DateField(blank=True, null=True, verbose_name='Конечная дата')),
                ('text', models.CharField(max_length=128, verbose_name='Сосотяние')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children.Child', verbose_name='Ребенок')),
            ],
            options={
                'verbose_name_plural': 'История состояния здоровья',
                'db_table': 'healths',
                'verbose_name': 'Истории состояния здоровья',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование')),
                ('type', models.IntegerField(blank=True, choices=[(0, 'Дошкольное'), (1, 'Школьное')], null=True, verbose_name='Тип учреждения')),
            ],
            options={
                'verbose_name_plural': ' Учреждения (Справочник)',
                'db_table': 'institutions',
                'verbose_name': 'Учреждение (Справочник)',
            },
        ),
        migrations.CreateModel(
            name='NoteHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_date', models.DateField(default=datetime.datetime.now, verbose_name='Начальная дата')),
                ('last_date', models.DateField(blank=True, null=True, verbose_name='Конечная дата')),
                ('text', models.CharField(max_length=256, verbose_name='Сосотяние')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children.Child', verbose_name='Ребенок')),
            ],
            options={
                'verbose_name_plural': 'История примечаний',
                'db_table': 'notes',
                'verbose_name': 'Истории примечаний',
            },
        ),
        migrations.CreateModel(
            name='RiskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_date', models.DateField(default=datetime.datetime.now, verbose_name='Начальная дата')),
                ('last_date', models.DateField(blank=True, null=True, verbose_name='Конечная дата')),
                ('group', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], verbose_name='Группа риска')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children.Child', verbose_name='Ребенок')),
            ],
            options={
                'verbose_name_plural': 'Группа риска',
                'db_table': 'risks',
                'verbose_name': 'Группа риска',
            },
        ),
        migrations.CreateModel(
            name='StudentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_date', models.DateField(default=datetime.datetime.now, verbose_name='Начальная дата')),
                ('last_date', models.DateField(blank=True, null=True, verbose_name='Конечная дата')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children.Child', verbose_name='Ребенок')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parameters.Grade', verbose_name='Класс')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parameters.Group', verbose_name='Группа')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameters.Institution', verbose_name='Учреждение')),
            ],
            options={
                'verbose_name_plural': 'История обучения',
                'db_table': 'students',
                'verbose_name': 'Истории обучения',
            },
        ),
        migrations.AddField(
            model_name='familystatushistory',
            name='status',
            field=models.ManyToManyField(to='parameters.GuideFamilyStatus'),
        ),
    ]
