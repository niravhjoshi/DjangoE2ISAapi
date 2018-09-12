from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins
from .serializers import EarningTypeSerializer
from earningtype.models import EarningTypes
from accounts.api.permissions import IsOwnerOnly
from django.views.generic import View

class EarningTypeDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = [IsOwnerOnly]
    # authentication_classes  = []
    queryset                = EarningTypes.objects.all()
    serializer_class        = EarningTypeSerializer
    lookup_field            = 'EarnType_id'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,reuest,*args,**kwargs):
        return self.destroy(reuest,*args,**kwargs)



class EarningTypeAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes      = [IsOwnerOnly]
    # authentication_classes  = []
    serializer_class        = EarningTypeSerializer


    def get_queryset(self):
        request = self.request
        qs = EarningTypes.objects.filter(UserName=request.user)
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(EarningTypeName__icontains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save(UserName=self.request.user)