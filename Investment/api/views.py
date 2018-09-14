from rest_framework.response import Response
from rest_framework import generics,mixins,permissions
from .serializers import InvestmentsSerializer
from Investment.models import InvestmentsEntry
from accounts.api.permissions import IsOwnerOnly
from django_filters.rest_framework import DjangoFilterBackend


class InvestmentEntryDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = [IsOwnerOnly]
    #authentication_classes  = [SessionAuthentication]
    queryset                = InvestmentsEntry.objects.all()
    serializer_class        = InvestmentsSerializer
    lookup_field            = 'InvestmentId'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



class InvestmentEntryAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes      = [IsOwnerOnly]
    serializer_class        = InvestmentsSerializer
    #
    def get_queryset(self):
        request = self.request
        #print (request.user)
        qs = InvestmentsEntry.objects.filter(UserName=self.request.user)
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(InvestType_Name__InvestmentTypeName__contains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save(UserName=self.request.user)
