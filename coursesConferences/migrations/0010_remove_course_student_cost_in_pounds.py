# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursesConferences', '0009_auto_20160307_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student_cost_in_pounds',
        ),
    ]
