# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-12 11:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0005_auto_20180412_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
