from rest_framework.response import Response
from rest_framework import generics,mixins,permissions
from .serializers import SharesEntrySerializer
from Shares.models import SharesEntry
from accounts.api.permissions import IsOwnerOnly
from django_filters.rest_framework import DjangoFilterBackend


class SharesEntryDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = [IsOwnerOnly]
    #authentication_classes  = [SessionAuthentication]
    queryset                = SharesEntry.objects.all()
    serializer_class        = SharesEntrySerializer
    lookup_field            = 'SharesID'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



class SharesEntryAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes      = [IsOwnerOnly]
    serializer_class        = SharesEntrySerializer
    #
    def get_queryset(self):
        request = self.request
        #print (request.user)
        qs = SharesEntry.objects.filter(UserName=self.request.user)
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Share_Tick_Name__contains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save(UserName=self.request.user)
