# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0011_auto_20190428_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ManyToManyField(to='properties.Category', verbose_name='category'),
        ),
    ]
