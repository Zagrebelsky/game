# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='town',
            name='wall_ap',
            field=models.IntegerField(null=True),
        ),
    ]