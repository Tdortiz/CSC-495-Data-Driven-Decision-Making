# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalRanking', '0006_auto_20171119_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normalized_complications',
            name='denominator',
        ),
        migrations.RemoveField(
            model_name='normalized_returns',
            name='denominator',
        ),
    ]
