# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-17 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_subtags_tag_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subtags',
            options={'ordering': ['tag_url'], 'verbose_name': 'Дополнительные теги', 'verbose_name_plural': 'Дополнительные теги'},
        ),
        migrations.AddField(
            model_name='fblocks',
            name='fb_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
