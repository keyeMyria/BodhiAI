# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-12 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0016_auto_20181007_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrefferredLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Student')),
            ],
        ),
    ]
