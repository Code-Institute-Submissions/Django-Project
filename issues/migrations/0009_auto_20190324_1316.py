# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-24 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0008_auto_20190323_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comments',
            new_name='issue',
        ),
    ]
