# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectversion',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='D:\\github\\saltops\\doc\\scripts\\', verbose_name='版本'),
        ),
    ]
