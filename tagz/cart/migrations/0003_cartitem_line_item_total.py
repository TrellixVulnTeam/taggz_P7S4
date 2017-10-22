# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-10 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170709_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='line_item_total',
            field=models.DecimalField(decimal_places=2, default=2000.0, max_digits=10),
            preserve_default=False,
        ),
    ]