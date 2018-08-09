# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Person
import json
from django.views.generic import View
from DjangoE2ISAapi.mixins import JsonResponseMixin
from django.core.serializers import serialize
# Create your views here.

class PersonSerializeListView(View):
    def get(self,request,*args,**kwargs):
        qs = Person.objects.all()
        json_data = Person.objects.all().serialize()
        #PersonListViewData = serialize("json",PerObj)
        #json_data = PersonListViewData
        return HttpResponse(json_data,content_type='application/json')

class PersonSerializDetailView(View):
    def get(self,request,*args,**kwargs):
        pid = self.kwargs['puser_id']
        obj = Person.objects.get(Pid=pid,id_id=1)
        print obj
        json_data=obj.serialize()
        print json_data
        return HttpResponse(json_data, content_type='application/json')

