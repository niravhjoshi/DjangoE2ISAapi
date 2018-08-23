# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from persons import models as personmodel

# Create your models here.
class SharesEntry(models.Model):
    Id = models.AutoField(primary_key=True)
    U_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    P_id =models.ForeignKey(personmodel.Person,on_delete=models.CASCADE)
    Share_Per_Name = models.CharField("PersonName", max_length=30, null=False)
    Share_Tick_Name =models.CharField("ShareTickName",max_length=20)
    Share_Count = models.IntegerField("Share Count",null=False,blank=False)
    sellTran =(('Sell','S'),('Buy','B'),)
    Share_Tran_Type = models.CharField("ShareTranType",max_length=1,null=False,choices=sellTran,blank=False,)
    Share_pershare_amt = models.FloatField("PerShareAmt",null=False,blank=False)
    Share_Buy_Sell_Date = models.DateField("Share Buy Sell Date", null=False, blank=False)
    Share_img = models.BinaryField(null=True)
    Share_FileName =models.CharField("FileName",max_length=300,null=True)
    Share_comm = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Id, \
               self.U_id,\
               self.P_id ,\
               self.Share_Per_Name,\
               self.Share_Tick_Name,\
               self.Share_Count,\
               self.Share_Tran_Type,\
               self.Share_pershare_amt,\
               self.Share_Buy_Sell_Date,\
               self.Share_FileName,\
               self.Share_comm or ""
