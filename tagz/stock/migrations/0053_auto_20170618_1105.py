# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-18 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0052_auto_20170618_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]