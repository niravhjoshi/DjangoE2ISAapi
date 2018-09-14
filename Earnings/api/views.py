from rest_framework.response import Response
from rest_framework import generics,mixins,permissions
from .serializers import EarningsSerializer
from Earnings.models import EarningsEntry
from accounts.api.permissions import IsOwnerOnly
from django_filters.rest_framework import DjangoFilterBackend


class EarningEntryDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = [IsOwnerOnly]
    #authentication_classes  = [SessionAuthentication]
    queryset                = EarningsEntry.objects.all()
    serializer_class        = EarningsSerializer
    lookup_field            = 'EarningsId'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



class EarningEntryAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes      = [IsOwnerOnly]
    serializer_class        = EarningsSerializer
    #
    def get_queryset(self):
        request = self.request
        #print (request.user)
        qs = EarningsEntry.objects.filter(UserName=self.request.user)
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Earning_Type_Name__EarningTypeName__contains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save(UserName=self.request.user)
