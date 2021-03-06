from rest_framework import serializers
import datetime
from investmtype.models import InvestTypes

class InvTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestTypes
        fields = [
            'UserName',
            'Invtype_id',
            'InvestmentTypeName',
            'InvestmentType_CDate'
        ]
        read_only_fields = ['UserName']

    def validate_invtype(self,value):
        if len(value) > 30:
            raise serializers.ValidationError("InvestTypeName should not be more than 30 Char")
        return value

