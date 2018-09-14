# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from persons import models as personmodel
import json
from django.core.serializers.json import DjangoJSONEncoder

def upload_file(instance, filename):
    return "shares/{user}/{filename}".format(user=instance.UserName, filename=filename)

class SharesQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(
            self.values('SharesID',
                        'UserName',
                        'PersonName',
                        'Share_Tick_Name',
                        'Share_Count',
                        'sellTran',
                        'Share_Tran_Type',
                        'Share_pershare_amt',
                        'Share_Buy_Sell_Date',
                        'Share_img',
                        'Share_comm'))

        print(list_values)
        return json.dumps(list_values, sort_keys=True, indent=1, cls=DjangoJSONEncoder)


class SharesManager(models.Manager):
    def get_queryset(self):
        return SharesQuerySet(self.model, using=self._db)



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
    Share_img = models.ImageField(upload_to=upload_file,null=True,blank=True)
    Share_comm = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.UserName) + str(self.PersonName) + str(self.Share_Tick_Name) + str(self.Share_Count) +str(self.sellTran)+ \
               str(self.Share_Tran_Type) + str(self.Share_pershare_amt) + str(self.Share_Buy_Sell_Date) + str(self.Share_img)+ \
               str(self.Share_comm)  or ""

    def serialize(self):
        data = {
            'SharesID': self.SharesID,
            'UserName': self.UserName,
            'PersonName': self.PersonName,
            'Share_Tick_Name': self.Share_Tick_Name,
            'Share_Count': self.Share_Count,
            'sellTran': self.sellTran,
            'Share_Tran_Type': self.Share_Tran_Type,
            'Share_pershare_amt': self.Share_pershare_amt,
            'Share_Buy_Sell_Date': self.Share_Buy_Sell_Date,
            'Share_img': self.Share_img,
            'Share_comm': self.Share_comm
        }
        data = json.dumps(data, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        return data

    @property
    def owner(self):
        return self.SharesID
