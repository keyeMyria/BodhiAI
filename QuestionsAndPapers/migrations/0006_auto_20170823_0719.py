# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-23 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsAndPapers', '0005_auto_20170822_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='klasstest',
            name='totalTime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sscklasstest',
            name='totalTime',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]