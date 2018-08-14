# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.serializers import serialize
from django.db import models
from django.conf import settings
import json
from django.utils.encoding import python_2_unicode_compatible
from django.core.serializers.json import DjangoJSONEncoder
# Create your models here.

'''
class MalePerson(models.Manager):
    def get_queryset(self):
        return super(MalePerson, self).get_queryset().filter(sex='M')

class FemalePerson(models.Manager):
    def get_queryset(self):
        return super(FemalePerson, self).get_queryset().filter(sex='F')

class NonePerson(models.Manager):
    def get_queryset(self):
        return super(NonePerson, self).get_queryset().filter(sex='N')

class IdandPidFilter(models.Manger,id,pid):
    def get_IdandPid(self):
        return super(IdandPidFilter,self).get_queryset().filter(id=id,Pid=pid)

class PersonNameSearch(models.Manager,name):
    def get_searchbyName(self):
        return super(PersonNameSearch,self).get_queryset().filter(PersonName = Name)

Class PersonGetBdata(models.Manager,date):
    def get_searchbyBDate(self):
        return super(PersonGetBdata,self).get_queryset().filter(Person_BDate=date)
'''
class PersonQuerySet(models.QuerySet):
    def serialize(self):
        list_values=list(self.values('id','Pid','PersonName','Person_sex','Person_BDate'))
        print list_values
        return json.dumps(list_values,sort_keys=True,indent=1,cls=DjangoJSONEncoder)

class PersonManager(models.Manager):
        def get_queryset(self):
            return PersonQuerySet(self.model,using=self._db)

@python_2_unicode_compatible
class Person(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL)
    Pid = models.AutoField(primary_key=True)
    PersonName = models.CharField("person's first name", max_length=30,null=False)
    SEX = (('M','Male'),('F','Female'), ('N','None'), )
    Person_sex = models.CharField(max_length=1,choices=SEX,null=False)
    Person_BDate = models.DateField(null=False)
    Person_CDate =  models.DateField(null=False,auto_now_add=True)
    objects = PersonManager()


    def __str__(self):
        return str(self.PersonName)+str(self.Pid)+str(self.SEX)+str(self.Person_BDate)+str(self.id_id) or ""

    def serialize(self):
        data={
            'id': self.id_id,
            'Pid': self.Pid,
            'PersonName': self.PersonName,
            'Person_sex': self.Person_sex,
            'Person_Bdate': self.Person_BDate
        }
        data = json.dumps(data,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
        return data

