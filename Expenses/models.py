# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from persons import models as personmodel
from expensetype import models as exptypemodel
# Create your models here.
class ExpensesEntry(models.Model):
    Id = models.AutoField(primary_key=True)
    U_id=models.ForeignKey(settings.AUTH_USER_MODEL)
    P_id =models.ForeignKey(personmodel.Person)
    Exp_Per_Name = models.CharField("PersonName", max_length=30, null=False)
    Exp_Type_Name = models.CharField("ExpType", max_length=30, null=False)
    Exp_Amt = models.FloatField(null=False,blank=False)
    Exp_Img = models.BinaryField(null=True)
    Exp_FileName =models.CharField("FileName",max_length=300,null=True)
    Exp_date = models.DateField("ExpenseDate",null=False,blank=False)
    Exp_comm = models.TextField()

    def __str__(self):
        return self.Id, \
               self.U_id,\
               self.P_id ,\
               self.Exp_Per_Name,\
               self.Exp_Type_Name,\
               self.Exp_Amt,\
               self.Exp_FileName,\
               self.Exp_date,\
               self.Exp_comm or ""
