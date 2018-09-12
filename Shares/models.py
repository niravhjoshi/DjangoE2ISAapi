# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from persons import models as personmodel

# Create your models here.
class SharesEntry(models.Model):
    SharesID = models.AutoField(primary_key=True)
    UserName=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    PersonName=models.ForeignKey(personmodel.Person,on_delete=models.CASCADE)
    Share_Tick_Name =models.CharField("ShareTickName",max_length=20)
    Share_Count = models.IntegerField("Share Count",null=False,blank=False)
    sellTran =(('Sell','S'),('Buy','B'),)
    Share_Tran_Type = models.CharField("ShareTranType",max_length=1,null=False,choices=sellTran,blank=False,)
    Share_pershare_amt = models.FloatField("PerShareAmt",null=False,blank=False)
    Share_Buy_Sell_Date = models.DateField("Share Buy Sell Date", null=False, blank=False)
    Share_img = models.ImageField(null=True,blank=True)
    Share_comm = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.UserName) + str(self.PersonName) + str(self.Share_Tick_Name) + str(self.Share_Count) +str(self.sellTran)+ \
               str(self.Share_Tran_Type) + str(self.Share_pershare_amt) + str(self.Share_Buy_Sell_Date) + str(self.Share_img)+ \
               str(self.Share_comm)  or ""
