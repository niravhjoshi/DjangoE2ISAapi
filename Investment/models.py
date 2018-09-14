# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from persons import models as personmodel
from investmtype import models as invtypemodel
import json
from django.core.serializers.json import DjangoJSONEncoder

def upload_file(instance, filename):
    return "investments/{user}/{filename}".format(user=instance.UserName, filename=filename)

class SharesQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(
            self.values('InvestmentId',
                        'UserName',
                        'PersonName',
                        'InvestType_Name',
                        'Inv_Init_Amt',
                        'Inv_Mat_Amt',
                        'Inv_ROI_PerYear',
                        'Inv_Date',
                        'Inv_Mat_Date',
                        'Inv_Due_Date',
                        'Inv_Img',
                        'Inv_comm'))

        print(list_values)
        return json.dumps(list_values, sort_keys=True, indent=1, cls=DjangoJSONEncoder)


class SharesManager(models.Manager):
    def get_queryset(self):
        return SharesQuerySet(self.model, using=self._db)



# Create your models here.
class InvestmentsEntry(models.Model):
    InvestmentId = models.AutoField(primary_key=True)
    UserName=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    PersonName =models.ForeignKey(personmodel.Person,on_delete=models.CASCADE)
    InvestType_Name =models.ForeignKey(invtypemodel.InvestTypes,on_delete=models.CASCADE)
    Inv_Init_Amt = models.FloatField("Init Amnt",null=False,blank=False)
    Inv_Mat_Amt = models.FloatField("Mature Amnt",null=False,blank=False)
    Inv_ROI_PerYear = models.FloatField("ROI in Percentage",null=False,blank=False)
    Inv_Date = models.DateField("Inv Date",null=False,blank=False)
    Inv_Mat_Date = models.DateField("Inv Mat Date",null=False,blank=False)
    Inv_Due_Date = models.DateField("Inv Due Date",null=False,blank=False)
    Inv_Img = models.ImageField(upload_to=upload_file,null=True,blank=True)
    Inv_comm = models.TextField()

    def __str__(self):
        return str(self.UserName) + str(self.PersonName) + str(self.InvestType_Name) + str(self.Inv_Init_Amt) +str(self.Inv_Mat_Amt)+ \
               str(self.Inv_ROI_PerYear) + str(self.Inv_Date) + str(self.Inv_Mat_Date) + str(self.Inv_Due_Date)+ \
               str(self.Inv_Img) + str(self.Inv_comm) or ""

    def serialize(self):
        data = {
            'InvestmentId': self.InvestmentId,
            'UserName': self.UserName,
            'PersonName': self.PersonName,
            'InvestType_Name': self.InvestType_Name,
            'Inv_Init_Amt': self.Inv_Init_Amt,
            'Inv_Mat_Amt': self.Inv_Mat_Amt,
            'Inv_ROI_PerYear': self.Inv_ROI_PerYear,
            'Inv_Date': self.Inv_Date,
            'Inv_Mat_Date': self.Inv_Mat_Date,
            'Inv_Due_Date': self.Inv_Due_Date,
            'Inv_Img': self.Inv_Img,
            'Inv_comm': self.Inv_comm
        }
        data = json.dumps(data, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        return data

    @property
    def owner(self):
        return self.InvestmentId
