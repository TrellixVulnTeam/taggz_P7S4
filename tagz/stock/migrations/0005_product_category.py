# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-22 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20170122_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock.Category'),
            preserve_default=False,
        ),
    ]
