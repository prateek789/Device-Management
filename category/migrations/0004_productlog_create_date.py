# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_productlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlog',
            name='create_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
