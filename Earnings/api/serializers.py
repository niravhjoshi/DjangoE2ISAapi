from rest_framework import serializers
import datetime
from Earnings.models import EarningsEntry
from persons.models import Person
from earningtype.models import EarningTypes


class EarningsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(EarningsSerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['PersonName'].queryset = Person.objects.filter(UserName=request_user)
        self.fields['Earning_Type_Name'].queryset = EarningTypes.objects.filter(UserName=request_user)
    class Meta:
        model = EarningsEntry
        fields = [
            'EarningsId',
            'UserName',
            'PersonName',
            'Earning_Type_Name',
            'Ear_Amt',
            'Ear_Img',
            'Ear_date',
            'Ear_comm'

        ]
        read_only_fields=['UserName'] # Get calls its gone be read only.


    # def validate_Ear_Amt(self,value):
    #     if len(value) > 20:
    #         raise serializers.ValidationError("Earning amount is way high 20 Char")
    #     return value
    def validate_ear_date(self, value):
        if datetime.datetime.strptime(value, '%Y-%m-%d'):
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD")
        return value


