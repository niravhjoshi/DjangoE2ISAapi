# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse,HttpResponse
from .models import Person
import json
from django.views.generic import View
from DjangoE2ISAapi.mixins import JsonResponseMixin
# Create your views here.

def person_detail_view(request):
    data = {
        "Name":"Nirav Joshi",
        "Age":34
    }
    json_Data = json.dumps(data)
    return HttpResponse(json_Data,content_type='application/json')

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        data = {
            "Name": "Nirav Joshi",
            "Age": 25
        }
        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data = {
            "count":1000,
            "content":"Something new data"
        }
        return self.render_to_json_response(data)

class PersonSerializeListView(View):
    def get(self,request,*args,**kwargs):
        PerObj = Person.objects.filter(id_id =1).all()
        PersonListViewData = serialize("json",PerObj)
        #print PersonListViewData
        ''' 
        personlistdata ={
            'PersonID':PerObj.Pid,
            'PersonName':PerObj.PersonName,
            'Person_Sex':PerObj.Person_sex,
            'Person_Bdate':PerObj.Person_BDate,
            'UserName':PerObj.user.username
        }
        '''
        json_data = PersonListViewData
        return HttpResponse(json_data,content_type='application/json')

class PersonSerializDetailView(View):
    def get(self,request,*args,**kwargs):
        pid = self.kwargs['puser_id']
        PerobjDetail = Person.objects.filter(Pid=pid,id_id=1).all()
        print PerobjDetail
        data=serialize("json",PerobjDetail)
        json_data=data
        return HttpResponse(json_data, content_type='application/json')

