# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_productlog_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlog',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
