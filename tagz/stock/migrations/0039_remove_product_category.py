# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0038_auto_20170505_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
