# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-21 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsAndPapers', '0002_auto_20170821_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sscklasstest',
            name='max_marks',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
