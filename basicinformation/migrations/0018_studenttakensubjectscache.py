# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-12 09:25
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0017_prefferredlanguage'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTakenSubjectsCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Student')),
            ],
        ),
    ]