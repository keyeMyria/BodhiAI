# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-21 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recommendations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concept',
            name='content',
        ),
        migrations.RemoveField(
            model_name='concept',
            name='question',
        ),
        migrations.DeleteModel(
            name='Concept',
        ),
    ]
