# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-22 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180921_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objectinfo',
            old_name='_id',
            new_name='id_openData',
        ),
    ]
