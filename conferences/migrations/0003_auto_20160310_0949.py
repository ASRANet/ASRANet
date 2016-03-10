# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_auto_20160310_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='one_day_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='conference',
            name='url',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]
