# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_subtags_delete_stag'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создан'),
            preserve_default=False,
        ),
    ]