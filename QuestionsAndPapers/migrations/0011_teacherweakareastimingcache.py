# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-04 12:04
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0007_auto_20180412_1728'),
        ('QuestionsAndPapers', '0010_auto_20180804_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherWeakAreasTimingCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('klass', models.CharField(max_length=100, null=True)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('timing', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('testids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Teacher')),
            ],
        ),
    ]