# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-30 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20161029_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='name',
            field=models.CharField(max_length=20, verbose_name='카페 이름'),
        ),
    ]
