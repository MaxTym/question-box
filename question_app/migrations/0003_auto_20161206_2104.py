# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_app', '0002_auto_20161206_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(default=0, null=True, to='question_app.Tag'),
        ),
    ]
