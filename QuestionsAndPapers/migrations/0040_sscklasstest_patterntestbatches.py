# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-04 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0013_school_logo'),
        ('QuestionsAndPapers', '0039_sscklasstest_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='sscklasstest',
            name='patternTestBatches',
            field=models.ManyToManyField(related_name='patternBatches', to='basicinformation.klass'),
        ),
    ]