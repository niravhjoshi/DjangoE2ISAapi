# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-14 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Investment', '0002_auto_20180912_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investmentsentry',
            old_name='Id',
            new_name='InvestmentId',
        ),
    ]
