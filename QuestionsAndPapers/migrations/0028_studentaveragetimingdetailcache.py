# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-14 18:14
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0011_studentdetails_email'),
        ('QuestionsAndPapers', '0027_auto_20180914_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAverageTimingDetailCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('chapter', models.CharField(max_length=100)),
                ('totalAttempted', models.IntegerField()),
                ('rightAverage', models.FloatField()),
                ('wrongAverage', models.FloatField()),
                ('rightTotal', models.IntegerField()),
                ('wrongTotal', models.IntegerField()),
                ('rightTotalTime', models.FloatField()),
                ('wrongTotalTime', models.FloatField()),
                ('allMarksIds', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Student')),
            ],
        ),
    ]
