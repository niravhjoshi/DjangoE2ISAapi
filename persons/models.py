# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Person(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL)
    Pid = models.AutoField(primary_key=True)
    PersonName = models.CharField("person's first name", max_length=30,null=False)
    SEX = (('M','Male'),('F','Female'), ('N','None'), )
    Person_sex = models.CharField(max_length=1,choices=SEX,null=False)
    Person_BDate = models.DateField(null=False)
    Person_CDate =  models.DateField(null=False,auto_now_add=True)

    def __str__(self):
        return self.PersonName or ""
