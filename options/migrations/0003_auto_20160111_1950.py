# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0002_option_tournament'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='tournament',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
    ]
