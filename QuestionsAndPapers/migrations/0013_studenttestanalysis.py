# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-07 08:36
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0007_auto_20180412_1728'),
        ('QuestionsAndPapers', '0012_auto_20180804_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTestAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('myPercent', models.FloatField()),
                ('klassAverage', models.FloatField()),
                ('klassAveragePercent', models.FloatField()),
                ('myPercentile', models.FloatField()),
                ('allKlassMarks', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), null=True, size=None)),
                ('freqAnswerId', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('freqAnswer', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('weakCategories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None)),
                ('weakAccuracies', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), null=True, size=None)),
                ('numRight', models.IntegerField()),
                ('numWrong', models.IntegerField()),
                ('numSkipped', models.IntegerField()),
                ('overallAccuracy', models.FloatField()),
                ('subjectwiseAccuracySub', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None)),
                ('subjectwiseAccuracy', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(max_length=50), null=True, size=None)),
                ('areaTimeCategory', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None)),
                ('areaTime', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), null=True, size=None)),
                ('hour', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('second', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionsAndPapers.SSCKlassTest')),
            ],
        ),
    ]
