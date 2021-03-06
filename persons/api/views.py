from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins,permissions
from .serializers import PersonSerializer
from persons.models import Person
from django.views.generic import View
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication
from accounts.api.permissions import IsOwnerOnly
from DjangoE2ISAapi.restconf.filters import IsOwnerFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  SearchFilter,OrderingFilter

class PersonDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = [IsOwnerOnly]
    #authentication_classes  = [SessionAuthentication]
    queryset                = Person.objects.all()
    serializer_class        = PersonSerializer


    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,reuest,*args,**kwargs):
        return self.destroy(reuest,*args,**kwargs)

# class CustomPagination(pagination.PageNumberPagination):
#     page_size = 2


class PersonAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes      = [IsOwnerOnly]
    serializer_class        = PersonSerializer
    queryset                = Person.objects.all()
    filter_backends         = (IsOwnerFilterBackend,SearchFilter,OrderingFilter)
    search_fields           = ('PersonName', 'Person_sex')

    #
    # def get_object(self):
    #     obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
    #     self.check_object_permissions(self.request, obj)
    #     return obj
    # def get_queryset(self):
    #     request = self.request
    #     #print (request.user)
    #     qs = Person.objects.filter(UserName=self.request.user)
    #     query = request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(PersonName__icontains=query)
    #     return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save(UserName=self.request.user)
    # def perform_update(self, serializer):
    #     pass



# class PersonListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self,request,format=None):
#         qs = Person.objects.all()
#         serializer = PersonSerializer(qs,many=True)
#         return Response(serializer.data)
#
# #CreateModelMixin for Handling POST data and List View Data
# #mixin.CreateModelMixin --> POST Method
# #mixin.UpdateModelMixin --> PUT Method
# #mixin.DestroyModelMixin --> DELETE Method
#
# #Create and List View Mixin
# class PersonAPIView(mixins.CreateModelMixin,generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     #queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
#     def get_queryset(self):
#         qs = Person.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(PersonName__icontains=query)
#         return qs
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
#     # def perform_create(self, serializer):
#     #     serializer.save(user = self.request.user)
#
# #We dont need this Create API view method as this already covered in the mixin
# # class PersonCreateAPIView(generics.CreateAPIView):
# #     permission_classes =        []
# #     authentication_classes =    []
# #     queryset =                  Person.objects.all()
# #     serializer_class =          PersonSerializer
#
# #There is simple way to define this method
# class PersonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes =        []
#     authentication_classes =    []
#     queryset =                  Person.objects.all()
#     serializer_class =          PersonSerializer
#     lookup_field =              'Pid'
#

#THis will be UpdateMix and Retrive View Mixin
# class PersonDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
#     permission_classes =        []
#     authentication_classes =    []
#     queryset =                  Person.objects.all()
#     serializer_class =          PersonSerializer
#     lookup_field =              'Pid'
#
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#
#     def patch(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

    #
    # def get_object(self,*args,**kwargs):
    #     kwargs = self.kwargs
    #     kw_Pid = kwargs.get('Pid')
    #     print kw_Pid
    #     return Person.objects.get(Pid=kw_Pid)

# class PersonUpdateAPIView(generics.UpdateAPIView):
#     permission_classes =        []
#     authentication_classes =    []
#     queryset =                  Person.objects.all()
#     serializer_class =          PersonSerializer
#     lookup_field = 'Pid'
#
#
# class PersonDeleteAPIView(generics.DestroyAPIView):
#     permission_classes =        []
#     authentication_classes =    []
#     queryset =                  Person.objects.all()
#     serializer_class =          PersonSerializer
#     lookup_field = 'Pid'
#
