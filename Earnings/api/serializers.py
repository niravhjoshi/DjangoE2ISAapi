from rest_framework import serializers
import datetime
from Earnings.models import EarningsEntry
from persons.models import Person
from earningtype.models import EarningTypes
from django.contrib.auth import get_user_model



class EarningsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(EarningsSerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['P_id'].queryset = Person.objects.filter(id_id=request_user)
        self.fields['Earning_Type_id'].queryset = EarningTypes.objects.filter(User_id=request_user)
    class Meta:
        model = EarningsEntry
        fields = [
            'Id',
            'U_id',
            'P_id',
            'Earning_Type_id',
            'Ear_Amt',
            'Ear_Img',
            'Ear_date',
            'Ear_comm'

        ]
        read_only_fields=['U_id'] # Get calls its gone be read only.


    def validate_Ear_Amt(self,value):
        if len(value) > 20:
            raise serializers.ValidationError("Earning amount is way high 20 Char")
        return value
    def validate_Ear_date(self,value):
        if datetime.datetime.strptime(value, '%Y-%m-%d'):
            raise serializers.ValidationError("Incorrect date format, should be YYYY-MM-DD")
        return value

