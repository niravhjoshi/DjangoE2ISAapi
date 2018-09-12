# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import python_2_unicode_compatible
import json

# Create your models here.
class InvTypeQuerySet(models.QuerySet):
    def serialize(self):
        list_value = list(self.values_list('UserName','Invtype_id','InvestmentTypeName','InvestmentType_CDate'))
        print (list_value)
        return json.dumps(list_value,sort_keys=True,indent=1,cls=DjangoJSONEncoder)

class InvTypeManager(models.Manager):
    def get_queryset(self):
        return InvTypeQuerySet(self.model,using=self._db)



class InvestTypes(models.Model):
    UserName = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Invtype_id = models.AutoField(primary_key=True)
    InvestmentTypeName = models.CharField("Investment's Type", max_length=30,null=False)
    InvestmentType_CDate =  models.DateField(null=False,auto_now_add=True)

    def __str__(self):
        return str(self.UserName) + str(self.Invtype_id) + str(self.InvestmentTypeName) or ""

    def serialize(self):
        data = {
            'UserName': self.UserName,
            'Invtype_id': self.Invtype_id,
            'InvestmentTypeName': self.InvestmentTypeName,
        }
        data = json.dumps(data, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        return data

    @property
    def owner(self):
        return self.UserName