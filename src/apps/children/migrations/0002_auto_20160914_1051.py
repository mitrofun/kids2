# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-14 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='child',
            unique_together=set([('last_name', 'first_name', 'middle_name', 'birthday')]),
        ),
    ]