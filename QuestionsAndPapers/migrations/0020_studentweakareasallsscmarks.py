# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-30 16:06
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0007_auto_20180412_1728'),
        ('QuestionsAndPapers', '0019_studentweakareascache_alltests'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentWeakAreasAllSSCMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('allTests', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('numTests', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Student')),
            ],
        ),
    ]
