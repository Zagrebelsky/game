# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('town', '0007_auto_20171103_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.BooleanField(default=False)),
                ('ap', models.IntegerField(default=0)),
                ('building_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='town.BuildingType')),
            ],
        ),
        migrations.RemoveField(
            model_name='town',
            name='wall',
        ),
        migrations.RemoveField(
            model_name='town',
            name='wall_ap',
        ),
        migrations.AddField(
            model_name='building',
            name='town_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='town.Town'),
        ),
    ]
