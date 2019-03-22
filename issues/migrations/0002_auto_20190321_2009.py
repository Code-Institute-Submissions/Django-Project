# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='comment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='issue',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
