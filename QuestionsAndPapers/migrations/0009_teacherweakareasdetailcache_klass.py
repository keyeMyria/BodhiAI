# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-04 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsAndPapers', '0008_auto_20180804_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherweakareasdetailcache',
            name='klass',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
