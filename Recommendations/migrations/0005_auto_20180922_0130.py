# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-21 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recommendations', '0004_auto_20180922_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concepts',
            name='content',
            field=models.ManyToManyField(blank=True, null=True, to='Recommendations.RecommendedContent'),
        ),
    ]
