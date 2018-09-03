from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins
from .serializers import ExpenseTypeSerializer
from expensetype.models import ExpenseType
from django.views.generic import View
from accounts.api.permissions import IsOwnerOnly

class ExpenseTypeDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = [IsOwnerOnly]
    # authentication_classes  = []
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
    permission_classes       = [IsOwnerOnly]
    #authentication_classes  = []
    serializer_class         = ExpenseTypeSerializer


    def get_queryset(self):
        request = self.request
        qs = ExpenseType.objects.filter(U_id=request.user)
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(ExpenseTypeName__icontains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save(U_id=self.request.user)
