# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-27 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0020_auto_20181022_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Student')),
            ],
        ),
    ]
