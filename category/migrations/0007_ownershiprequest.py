# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 10:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0006_productlog_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnershipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_product', to='category.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ownership_request',
            },
        ),
    ]
