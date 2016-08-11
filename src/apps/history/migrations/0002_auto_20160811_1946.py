# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-11 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paramhistory',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history_institution', to='dictionaries.Dictionary', verbose_name='Учреждение'),
        ),
        migrations.AlterField(
            model_name='paramhistory',
            name='note',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Примечание'),
        ),
    ]
