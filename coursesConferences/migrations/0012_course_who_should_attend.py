# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-08 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesConferences', '0011_auto_20160307_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='who_should_attend',
            field=models.CharField(default=0, max_length=2000),
            preserve_default=False,
        ),
    ]