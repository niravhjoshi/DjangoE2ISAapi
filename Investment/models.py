# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from persons import models as personmodel
from investmtype import models as invtypemodel
# Create your models here.
class InvestmentsEntry(models.Model):
    Id = models.AutoField(primary_key=True)
    U_id=models.ForeignKey(settings.AUTH_USER_MODEL)
    P_id =models.ForeignKey(personmodel.Person)
    Inv_Per_Name = models.CharField("PersonName", max_length=30, null=False)
    Inv_Type_Name = models.CharField("InvType", max_length=30, null=False)
    Inv_Init_Amt = models.FloatField("Init Amnt",null=False,blank=False)
    Inv_Mat_Amt = models.FloatField("Mature Amnt",null=False,blank=False)
    Inv_ROI_PerYear = models.FloatField("ROI in Percentage",null=False,blank=False)
    Inv_Date = models.DateField("Inv Date",null=False,blank=False)
    Inv_Mat_Date = models.DateField("Inv Mat Date",null=False,blank=False)
    Inv_Due_Date = models.DateField("Inv Due Date",null=False,blank=False)
    Inv_Img = models.BinaryField(null=True)
    Inv_FileName =models.CharField("FileName",max_length=300,null=True)
    Inv_comm = models.TextField()

    def __str__(self):
        return self.Id, \
               self.U_id,\
               self.P_id ,\
               self.Inv_Per_Name,\
               self.Inv_Type_Name,\
               self.Inv_Init_Amt,\
               self.Inv_Mat_Amt,\
               self.Inv_Date,\
               self.Inv_Mat_Date,\
               self.Inv_Due_Date,\
               self.Inv_FileName,\
               self.Inv_comm or ""
