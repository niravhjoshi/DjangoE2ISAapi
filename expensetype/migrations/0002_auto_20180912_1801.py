# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-12 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensetype', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensetype',
            old_name='U_id',
            new_name='UserName',
        ),
    ]