# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import portal.models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20160213_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextra',
            name='prof_pic',
            field=models.ImageField(blank=True, max_length=300, upload_to=portal.models.rename_file),
        ),
    ]
