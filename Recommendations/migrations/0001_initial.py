# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-21 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('QuestionsAndPapers', '0030_auto_20180920_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('chapter', models.FloatField(blank=True, null=True)),
                ('concept_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendedContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('lang', models.CharField(max_length=50)),
                ('contentType', models.CharField(max_length=100)),
                ('chapter', models.FloatField()),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='concept',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Recommendations.RecommendedContent'),
        ),
        migrations.AddField(
            model_name='concept',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='QuestionsAndPapers.SSCquestions'),
        ),
    ]
