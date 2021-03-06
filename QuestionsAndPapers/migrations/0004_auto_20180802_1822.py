# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-02 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0007_auto_20180412_1728'),
        ('QuestionsAndPapers', '0003_auto_20180802_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherbatchweakareas',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacherbatchweakareas',
            name='batch',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacherbatchweakareas',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacherbatchweakareas',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
