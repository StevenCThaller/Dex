# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-21 02:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dex_app', '0007_auto_20181120_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moves',
            name='category',
        ),
        migrations.RemoveField(
            model_name='moves',
            name='tipe',
        ),
    ]
