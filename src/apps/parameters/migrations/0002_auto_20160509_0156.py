# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 01:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='familystatushistory',
            options={'verbose_name': 'Истории статусов семей', 'verbose_name_plural': 'История статуса семьи'},
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': 'Класс обучения (Справочник)', 'verbose_name_plural': 'Классы обучения (Справочник)'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Возрастная группа (Справочник)', 'verbose_name_plural': 'Возрастные группы (Справочник)'},
        ),
        migrations.AlterModelOptions(
            name='guidefamilystatus',
            options={'verbose_name': 'Статус семьи (Справочник)', 'verbose_name_plural': 'Статус семьи (Справочник)'},
        ),
        migrations.AlterModelOptions(
            name='healthhistory',
            options={'verbose_name': 'Истории состояния здоровья', 'verbose_name_plural': 'История состояния здоровья'},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'verbose_name': 'Учреждение (Справочник)', 'verbose_name_plural': 'Учреждения (Справочник)'},
        ),
        migrations.AlterModelOptions(
            name='notehistory',
            options={'verbose_name': 'Истории примечаний', 'verbose_name_plural': 'История примечаний'},
        ),
        migrations.AlterModelOptions(
            name='studenthistory',
            options={'verbose_name': 'Истории обучения', 'verbose_name_plural': 'История обучения'},
        ),
    ]
