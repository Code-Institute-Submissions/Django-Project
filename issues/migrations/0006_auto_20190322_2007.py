# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-22 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_auto_20190322_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
