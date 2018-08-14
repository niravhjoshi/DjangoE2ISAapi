from rest_framework.views import APIView
from rest_framework.response import Response
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

