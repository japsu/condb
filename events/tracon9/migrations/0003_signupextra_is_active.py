# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracon9', '0002_auto_20160306_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupextra',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
