# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-21 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recommendations', '0003_concepts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concepts',
            name='question',
        ),
        migrations.RemoveField(
            model_name='concepts',
            name='content',
        ),
        migrations.AddField(
            model_name='concepts',
            name='content',
            field=models.ManyToManyField(to='Recommendations.RecommendedContent'),
        ),
    ]
