# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-17 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
