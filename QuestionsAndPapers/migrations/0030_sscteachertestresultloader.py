# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-12 08:04
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0013_school_logo'),
        ('QuestionsAndPapers', '0029_auto_20171121_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='SscTeacherTestResultLoader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average', models.FloatField()),
                ('percentAverage', models.FloatField()),
                ('grade_a', models.IntegerField(default=0)),
                ('grade_b', models.IntegerField(default=0)),
                ('grade_c', models.IntegerField(default=0)),
                ('grade_d', models.IntegerField(default=0)),
                ('grade_e', models.IntegerField(default=0)),
                ('grade_f', models.IntegerField(default=0)),
                ('grade_s', models.IntegerField(default=0)),
                ('skipped', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('skippedFreq', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('problemQuestions', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('problemQuestionsFreq', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('onlineMarks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionsAndPapers.SSCOnlineMarks')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Teacher')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionsAndPapers.SSCKlassTest')),
            ],
        ),
    ]
