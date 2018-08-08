# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class ExpenseType(models.Model):
    U_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    id = models.AutoField(primary_key=True)
    ExpenseTypeName = models.CharField("Expense's Type", max_length=30,null=False)
    ExpenseType_CDate =  models.DateField(null=False,auto_now_add=True)

    def __str__(self):
        return self.U_id,self.id,self.ExpenseTypeName or ""