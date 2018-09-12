# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import python_2_unicode_compatible
import json
# Create your models here.

class ExpenseTypeQuerySet(models.QuerySet):
    def serialize(self):
        list_value = list(self.values_list('UserName','ExpenseType_id','ExpenseTypeName','ExpenseType_CDate'))
        print (list_value)
        return json.dumps(list_value,sort_keys=True,indent=1,cls=DjangoJSONEncoder)

class ExpenseTypeManager(models.Manager):
    def get_queryset(self):
        return ExpenseTypeQuerySet(self.model,using=self._db)

@python_2_unicode_compatible
class ExpenseType(models.Model):
    UserName = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ExpenseType_id = models.AutoField(primary_key=True)
    ExpenseTypeName = models.CharField("Expense's Type", max_length=30,null=False)
    ExpenseType_CDate =  models.DateField(null=False,auto_now_add=True)
    objects = ExpenseTypeManager()

    def __str__(self):
        return str(self.UserName) + str(self.ExpenseType_id) + str(self.ExpenseTypeName) or ""

    def serialize(self):
        data = {
            'UserName': self.UserName,
            'ExpenseType_id': self.ExpenseType_id,
            'ExpenseTypeName': self.ExpenseTypeName,
        }
        data = json.dumps(data, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        return data

    @property
    def owner(self):
        return self.UserName