# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0015_auto_20190429_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='properties.Category'),
        ),
    ]
