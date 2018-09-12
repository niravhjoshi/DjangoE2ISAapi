from rest_framework import serializers
import datetime
from persons.models import Person

'''
#Serializers can convert ---> Json
#Serializers can validate data
'''
#class PersonCustomSerilizer(serializers.Serializer):
#    text_field = serializers.CharField()

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'UserName',
            'PersonId',
            'PersonName',
            'Person_Image',
            'Person_sex',
            'Person_BDate',
            'Person_CDate'
        ]
        read_only_fields=['UserName'] # Get calls its gone be read only.


    def validate_personName(self,value):
        if len(value) > 30:
            raise serializers.ValidationError("PersonName should not be more than 30 Char")
        return value
    def validate_personsex(self,value):
        if value not in ['M','F','N']:
            raise  serializers.ValidationError("PersonSex should be M F or N")
        return value
    def validate_personbdate(self,value):
        if datetime.datetime.strptime(value, '%Y-%m-%d'):
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD")
        return value
    def validate_personimg(self,value):
        pass
