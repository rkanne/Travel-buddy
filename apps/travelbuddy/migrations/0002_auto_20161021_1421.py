# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelbuddy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='travel_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trips',
            name='travel_to',
            field=models.DateField(),
        ),
    ]
