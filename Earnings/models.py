# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from persons import models as personmodel
from earningtype import models as eartypemodel
# Create your models here.
class EarningsEntry(models.Model):
    Id = models.AutoField(primary_key=True)
    U_id=models.ForeignKey(settings.AUTH_USER_MODEL)
    P_id =models.ForeignKey(personmodel.Person)
    Ear_Per_Name = models.CharField("PersonName",max_length=30,null=False)
    Ear_Type_Name =models.CharField("EarninType",max_length=30,null=False)
    Ear_Amt = models.FloatField(null=False,blank=False)
    Ear_Img = models.BinaryField(null=True)
    Ear_FileName =models.CharField("FileName",max_length=300,null=True)
    Ear_date = models.DateField("ExpenseDate",null=False,blank=False)
    Ear_comm = models.TextField()

    def __str__(self):
        return self.Id, \
               self.U_id,\
               self.P_id ,\
               self.Ear_Per_Name,\
               self.Ear_Type_Name,\
               self.Ear_Amt,\
               self.Ear_FileName,\
               self.Ear_date,\
               self.Ear_comm or ""

