# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validation',
            name='first',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='validation',
            name='last',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='validation',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
