# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-20 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watershed', '0007_auto_20170419_2051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ffinfo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='manmadefeature',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='naturalfeature',
            options={'managed': False},
        ),
    ]