# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-30 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsAndPapers', '0048_auto_20180130_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sscquestions',
            name='language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Bi', 'Bi')], max_length=20, null=True),
        ),
    ]
