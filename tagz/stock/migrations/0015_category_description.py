# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_auto_20170210_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, default='medium', max_length=100, null=True),
        ),
    ]
