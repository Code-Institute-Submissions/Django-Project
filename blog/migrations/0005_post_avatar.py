# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-30 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190329_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avatar',
            field=models.ImageField(default='/media/profile_images/default.png', upload_to=''),
        ),
    ]