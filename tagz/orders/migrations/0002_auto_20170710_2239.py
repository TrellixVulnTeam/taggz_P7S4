# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-10 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestcheckout',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]