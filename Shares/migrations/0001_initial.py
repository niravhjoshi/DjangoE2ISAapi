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
            name='SharesEntry',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Share_Per_Name', models.CharField(max_length=30, verbose_name='PersonName')),
                ('Share_Tick_Name', models.CharField(max_length=20, verbose_name='ShareTickName')),
                ('Share_Count', models.IntegerField(verbose_name='Share Count')),
                ('Share_Tran_Type', models.CharField(choices=[('Sell', 'S'), ('Buy', 'B')], max_length=1, verbose_name='ShareTranType')),
                ('Share_pershare_amt', models.FloatField(verbose_name='PerShareAmt')),
                ('Share_Buy_Sell_Date', models.DateField(verbose_name='Share Buy Sell Date')),
                ('Share_img', models.BinaryField(null=True)),
                ('Share_FileName', models.CharField(max_length=300, null=True, verbose_name='FileName')),
                ('Share_comm', models.TextField(blank=True, null=True)),
                ('P_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person')),
                ('U_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
