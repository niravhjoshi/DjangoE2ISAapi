from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PersonSerializer
from persons.models import Person

#from django.views.generic import View

class PersonListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self,request,format=None):
        qs = Person.objects.all()
        serializer = PersonSerializer(qs,many=True)
        return Response(serializer.data)

class PersonAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    #queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        qs = Person.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(PersonName__icontains=query)
        return qs

class PersonCreateAPIView(generics.CreateAPIView):
    permission_classes =        []
    authentication_classes =    []
    queryset =                  Person.objects.all()
    serializer_class =          PersonSerializer

class PersonDetailAPIView(generics.RetrieveAPIView):
    permission_classes =        []
    authentication_classes =    []
    queryset =                  Person.objects.all()
    serializer_class =          PersonSerializer
    lookup_field =              'Pid'
    #
    # def get_object(self,*args,**kwargs):
    #     kwargs = self.kwargs
    #     kw_Pid = kwargs.get('Pid')
    #     print kw_Pid
    #     return Person.objects.get(Pid=kw_Pid)

class PersonUpdateAPIView(generics.UpdateAPIView):
    permission_classes =        []
    authentication_classes =    []
    queryset =                  Person.objects.all()
    serializer_class =          PersonSerializer
    lookup_field = 'Pid'


class PersonDeleteAPIView(generics.DestroyAPIView):
    permission_classes =        []
    authentication_classes =    []
    queryset =                  Person.objects.all()
    serializer_class =          PersonSerializer
    lookup_field = 'Pid'

