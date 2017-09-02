# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-27 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicinformation', '0011_auto_20170816_0246'),
        ('QuestionsAndPapers', '0012_auto_20170827_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryQuestionsHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.CharField(max_length=6)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicinformation.Teacher')),
            ],
        ),
    ]