# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-22 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Variation',
        ),
    ]