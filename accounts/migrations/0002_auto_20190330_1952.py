# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-30 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='default.png',
                                    upload_to='profile_images'),
        ),
    ]
