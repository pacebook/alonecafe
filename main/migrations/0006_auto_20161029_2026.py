# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-29 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161029_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafephoto',
            name='cafe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='main.Cafe'),
        ),
    ]
