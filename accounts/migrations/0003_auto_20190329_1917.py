# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190328_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='profile_images/default.png', upload_to='profile_images'),
        ),
    ]