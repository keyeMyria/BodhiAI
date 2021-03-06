# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-22 12:06
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0019_studenttaptracker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studenttaptracker',
            name='events',
        ),
        migrations.RemoveField(
            model_name='studenttaptracker',
            name='subjects',
        ),
        migrations.AddField(
            model_name='studenttaptracker',
            name='accuractyData',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='studenttaptracker',
            name='averageTimeData',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='studenttaptracker',
            name='learnData',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='studenttaptracker',
            name='performancdData',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='studenttaptracker',
            name='progressData',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='studenttaptracker',
            name='testData',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='studenttaptracker',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studenttaptracker',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Student'),
        ),
    ]
