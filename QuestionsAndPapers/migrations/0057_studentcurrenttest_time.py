# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-15 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsAndPapers', '0056_studentcurrenttest'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcurrenttest',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
