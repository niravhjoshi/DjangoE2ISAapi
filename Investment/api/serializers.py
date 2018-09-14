from rest_framework import serializers
import datetime
from Investment.models import InvestmentsEntry
from persons.models import Person
from investmtype.models import InvestTypes


class InvestmentsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(InvestmentsSerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['PersonName'].queryset = Person.objects.filter(UserName=request_user)
        self.fields['InvestType_Name'].queryset = InvestTypes.objects.filter(UserName=request_user)
    class Meta:
        model = InvestmentsEntry
        fields = [
            'InvestmentId',
            'UserName',
            'PersonName',
            'InvestType_Name',
            'Inv_Init_Amt',
            'Inv_Mat_Amt',
            'Inv_ROI_PerYear',
            'Inv_Date',
            'Inv_Mat_Date',
            'Inv_Due_Date',
            'Inv_Img',
            'Inv_comm'

        ]
        read_only_fields=['UserName'] # Get calls its gone be read only.


    def validate_Inv_Date_date(self, value):
        if datetime.datetime.strptime(value, '%Y-%m-%d'):
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD")
        return value
    def validate_Inv_Mat_Date_date(self, value):
        if datetime.datetime.strptime(value, '%Y-%m-%d'):
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD")
        return value
    def validate_Inv_Due_Date_date(self, value):
        if datetime.datetime.strptime(value, '%Y-%m-%d'):
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD")
        return value


