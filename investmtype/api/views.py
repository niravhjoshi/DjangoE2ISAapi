from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins
from .serializers import InvTypeSerializer
from investmtype.models import InvestTypes
from django.views.generic import View
from accounts.api.permissions import IsOwnerOnly

class InvTypeDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = [IsOwnerOnly]
    # authentication_classes  = []
    queryset                = InvestTypes.objects.all()
    serializer_class        = InvTypeSerializer
    lookup_field            = 'Invtype_id'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,reuest,*args,**kwargs):
        return self.destroy(reuest,*args,**kwargs)



class InvTypeAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes      = [IsOwnerOnly]
    # authentication_classes  = []
    serializer_class        = InvTypeSerializer


    def get_queryset(self):
        request = self.request
        qs = InvestTypes.objects.filter(UserName=self.request.user)
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(InvestmentTypeName__icontains=query)
        return qs


    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save(UserName=self.request.user)
