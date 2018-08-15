# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-02 08:23
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsAndPapers', '0002_studentsmarttesttopics'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherBatchWeakAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=100)),
                ('weak_sections', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='sscquestions',
            name='section_category',
            field=models.CharField(choices=[('General-Intelligence', 'General-Intelligence'), ('General-Knowledge', 'General-Knowledge'), ('Quantitative-Analysis', 'Quantitative-Analysis'), ('English', 'English'), ('Defence-English', 'Defence-English'), ('Defence-Physics', 'Defence-Physics'), ('GroupX-Maths', 'GroupX-Maths'), ('Defence-GK-CA', 'Defence-GK-CA'), ('MathsIITJEE10', 'MathsIITJEE10'), ('MathsIITJEE11', 'MathsIITJEE11'), ('MathsIITJEE12', 'MathsIITJEE12'), ('ChemistryIITJEE10', 'ChemistryIITJEE10'), ('ChemistryIITJEE11', 'ChemistryIITJEE11'), ('ChemistryIITJEE12', 'ChemistryIITJEE12'), ('PhysicsIITJEE10', 'PhysicsIITJEE10'), ('PhysicsIITJEE11', 'PhysicsIITJEE11'), ('PhysicsIITJEE12', 'PhysicsIITJEE12'), ('Design and analysis of algorithm', 'Design and analysis of algorithm')], max_length=70),
        ),
    ]