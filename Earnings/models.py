# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from persons import models as personmodel
from earningtype import models as eartypemodel
import json
from django.core.serializers.json import DjangoJSONEncoder


def upload_file(instance, filename):
    return "earnings/{user}/{filename}".format(user=instance.id, filename=filename)


class EarningsQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(
            self.values('Id', 'U_id', 'P_id', 'Earning_Type_id', 'Ear_Amt', 'Ear_Img', 'Ear_date', 'Ear_comm'))
        print(list_values)
        return json.dumps(list_values, sort_keys=True, indent=1, cls=DjangoJSONEncoder)


class EarningssManager(models.Manager):
    def get_queryset(self):
        return EarningsQuerySet(self.model, using=self._db)


# Create your models here.
class EarningsEntry(models.Model):
    Id = models.AutoField(primary_key=True)
    U_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    P_id =models.ForeignKey(personmodel.Person,on_delete=models.CASCADE)
    Earning_Type_id = models.ForeignKey(eartypemodel.EarningTypes,on_delete=models.CASCADE)
    Ear_Amt = models.FloatField(null=False,blank=False)
    Ear_Img = models.ImageField(null=True,blank=True)
    Ear_date = models.DateField("ExpenseDate",null=False,blank=False)
    Ear_comm = models.TextField()
    objects = EarningssManager()

    def __str__(self):
        return str(self.U_id) + str(self.P_id) + str(self.Ear_Amt) + str(self.Ear_Img) +str(self.Ear_Img)+str(self.Earning_Type_id)+ \
               str(self.Ear_date) + str(self.Ear_comm) + str(self.Id) or ""

    def serialize(self):
        data={
            'Id': self.Id,
            'U_id': self.U_id,
            'P_id': self.P_id,
            'Earning_Type_id': self.Earning_Type_id,
            'Ear_Amt': self.Ear_Amt,
            'Ear_Img': self.Ear_Img,
            'Ear_date': self.Ear_date,
            'Ear_comm': self.Ear_comm
        }
        data = json.dumps(data,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
        return data


    @property
    def owner(self):
        return self.Id
