# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-11 12:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20180111_0855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]