# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comicreader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comicdatabase',
            name='fileup',
        ),
        migrations.AlterField(
            model_name='comicdatabase',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
