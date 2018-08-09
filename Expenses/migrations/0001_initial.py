# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-07 11:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0002_auto_20180807_1430'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpensesEntry',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Exp_Per_Name', models.CharField(max_length=30, verbose_name='PersonName')),
                ('Exp_Type_Name', models.CharField(max_length=30, verbose_name='ExpType')),
                ('Exp_Amt', models.FloatField()),
                ('Exp_Img', models.BinaryField(null=True)),
                ('Exp_FileName', models.CharField(max_length=300, null=True, verbose_name='FileName')),
                ('Exp_date', models.DateField(verbose_name='ExpenseDate')),
                ('Exp_comm', models.TextField()),
                ('P_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person')),
                ('U_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]