# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0003_auto_20171103_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='town',
            name='wall_ap',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
