from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins
from .serializers import ExpenseTypeSerializer
from expensetype.models import ExpenseType
from django.views.generic import View

class ExpenseTypeDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = []
    authentication_classes  = []
    queryset                = ExpenseType.objects.all()
    serializer_class        = ExpenseTypeSerializer
    lookup_field            = 'ExpenseType_id'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,reuest,*args,**kwargs):
        return self.destroy(reuest,*args,**kwargs)



class ExpenseTypeAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = ExpenseTypeSerializer


    def get_queryset(self):
        request = self.request
        qs = ExpenseType.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(ExpenseTypeName__icontains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
