# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_remove_notification_desktop_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
