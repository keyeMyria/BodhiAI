# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-21 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsAndPapers', '0030_auto_20180920_1909'),
        ('Recommendations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('chapter', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='recommendedcontent',
            name='weakness',
        ),
        migrations.AddField(
            model_name='recommendedcontent',
            name='source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='concept',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recommendations.RecommendedContent'),
        ),
        migrations.AddField(
            model_name='concept',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuestionsAndPapers.SSCquestions'),
        ),
    ]
