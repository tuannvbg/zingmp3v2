# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-04 03:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songlyrics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
