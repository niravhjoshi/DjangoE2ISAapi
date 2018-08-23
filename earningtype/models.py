# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import python_2_unicode_compatible


class EarningTypeQuerySet(models.QuerySet):
    def serialize(self):
        list_values=list(self.values('User_id','EarnType_id','EarningTypeName'))
        print (list_values)
        return json.dumps(list_values,sort_keys=True,indent=1,cls=DjangoJSONEncoder)


class EarningTypeManager(models.Manager):
        def get_queryset(self):
            return EarningTypeQuerySet(self.model,using=self._db)

@python_2_unicode_compatible
class EarningTypes(models.Model):
    User_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    EarnType_id = models.AutoField(primary_key=True)
    EarningTypeName = models.CharField("Earning's Type", max_length=30,null=False)
    EarningType_CDate = models.DateField(null=False,auto_now_add=True)
    objects = EarningTypeManager()

    def __str__(self):
        return str(self.User_id)+str(self.EarnType_id)+str(self.EarningTypeName) or ""

    def serialize(self):
        data = {
            'User_id': self.User_id_id,
            'EarnType_id': self.EarnType_id,
            'EarningTypeName': self.EarningTypeName,
        }
        data = json.dumps(data, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        return data