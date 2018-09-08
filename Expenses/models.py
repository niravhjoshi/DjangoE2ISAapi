# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from persons import models as personmodel
from expensetype import models as exptypemodel
import json
from django.core.serializers.json import DjangoJSONEncoder


def upload_file(instance, filename):
    return "expenses/{user}/{filename}".format(user=instance.id, filename=filename)


class ExpensesQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(
            self.values('Id', 'U_id', 'P_id', 'Exp_Type_id', 'Exp_Amt', 'Exp_Img', 'Exp_FileName', 'Exp_date',
                        'Exp_comm'))
        print(list_values)
        return json.dumps(list_values, sort_keys=True, indent=1, cls=DjangoJSONEncoder)


class ExpensesManager(models.Manager):
    def get_queryset(self):
        return ExpensesQuerySet(self.model, using=self._db)


# Create your models here.
class ExpensesEntry(models.Model):
    Id          = models.AutoField(primary_key=True)
    U_id        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    P_id        = models.ForeignKey(personmodel.Person, on_delete=models.CASCADE)
    Exp_Type_id = models.ForeignKey(exptypemodel.ExpenseType, on_delete=models.CASCADE)
    Exp_Amt     = models.FloatField(null=False, blank=False)
    Exp_Img     = models.ImageField(null=True, blank=True)
    Exp_date    = models.DateField("ExpenseDate", null=False, blank=False)
    Exp_comm    = models.TextField()
    objects     = ExpensesManager()

    def __str__(self):
        return str(self.U_id) + str(self.P_id) + str(self.Exp_Type_id) + str(self.Exp_Img) + \
               str(self.Exp_Amt) + str(self.Exp_date) + str(self.Exp_comm) + str(self.Id) or ""


    def serialize(self):
        data={
            'Id': self.Id,
            'U_id': self.U_id,
            'P_id': self.P_id,
            'Exp_Type_id': self.Exp_Type_id,
            'Exp_Amt': self.Exp_Amt,
            'Exp_Img': self.Exp_Img,
            'Exp_date': self.Exp_date,
            'Exp_comm': self.Exp_comm
        }
        data = json.dumps(data,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
        return data


    @property
    def owner(self):
        return self.Id