# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
class EarningTypes(models.Model):
    U_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    id = models.AutoField(primary_key=True)
    EarningTypeName = models.CharField("Earning's Type", max_length=30,null=False)
    EarningType_CDate =  models.DateField(null=False,auto_now_add=True)

    def __str__(self):
        return self.U_id,self.id,self.EarningTypeName or ""