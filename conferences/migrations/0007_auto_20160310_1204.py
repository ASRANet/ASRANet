# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0006_venue_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='address2',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
