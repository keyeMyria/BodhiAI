# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-13 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsAndPapers', '0052_auto_20180213_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sscklasstest',
            name='sub',
            field=models.CharField(choices=[('General-Intelligence', 'General-Intelligence'), ('General-Knowledge', 'General-Knowledge'), ('Quantitative-Analysis', 'Quantitative-Analysis'), ('English', 'English'), ('Defence-English', 'Defence-English'), ('Defence-Physics', 'Defence-Physics'), ('GroupX-Maths', 'GroupX-Maths'), ('Defence-GK-CA', 'Defence-GK-CA'), ('SSCMultipleSections', 'SSCMultipleSections'), ('Defence-MultipleSubjects', 'Defence-MultipleSubjects')], max_length=70),
        ),
    ]