# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from persons import models as personmodel
from investmtype import models as invtypemodel
# Create your models here.
class InvestmentsEntry(models.Model):
    Id = models.AutoField(primary_key=True)
    UserName=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    PersonName =models.ForeignKey(personmodel.Person,on_delete=models.CASCADE)
    InvestType_Name =models.ForeignKey(invtypemodel.InvestTypes,on_delete=models.CASCADE)
    Inv_Init_Amt = models.FloatField("Init Amnt",null=False,blank=False)
    Inv_Mat_Amt = models.FloatField("Mature Amnt",null=False,blank=False)
    Inv_ROI_PerYear = models.FloatField("ROI in Percentage",null=False,blank=False)
    Inv_Date = models.DateField("Inv Date",null=False,blank=False)
    Inv_Mat_Date = models.DateField("Inv Mat Date",null=False,blank=False)
    Inv_Due_Date = models.DateField("Inv Due Date",null=False,blank=False)
    Inv_Img = models.ImageField(null=True,blank=True)
    Inv_comm = models.TextField()

    def __str__(self):
        return str(self.UserName) + str(self.PersonName) + str(self.InvestType_Name) + str(self.Inv_Init_Amt) +str(self.Inv_Mat_Amt)+ \
               str(self.Inv_ROI_PerYear) + str(self.Inv_Date) + str(self.Inv_Mat_Date) + str(self.Inv_Due_Date)+ \
               str(self.Inv_Img) + str(self.Inv_comm) or ""
