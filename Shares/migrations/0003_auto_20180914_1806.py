# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-14 12:36
from __future__ import unicode_literals

import Shares.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shares', '0002_auto_20180912_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharesentry',
            name='Share_img',
            field=models.ImageField(blank=True, null=True, upload_to=Shares.models.upload_file),
        ),
    ]