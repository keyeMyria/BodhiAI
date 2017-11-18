# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-14 08:11
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0012_auto_20171004_1833'),
        ('QuestionsAndPapers', '0027_auto_20171024_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSCOfflineMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rightAnswers', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None)),
                ('wrongAnswers', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None)),
                ('allAnswers', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None)),
                ('skippedAnswers', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None)),
                ('marks', models.DecimalField(decimal_places=2, max_digits=4)),
                ('testTaken', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionsAndPapers.SSCKlassTest')),
            ],
        ),
    ]