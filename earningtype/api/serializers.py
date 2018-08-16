from rest_framework import serializers
import datetime
from earningtype.models import EarningTypes

class EarningTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EarningTypes
        fields = [
            'User_id',
            'EarnType_id',
            'EarningTypeName',
            'EarningType_CDate'
        ]


    def validate_earningtype(self,value):
        if len(value) > 30:
            raise serializers.ValidationError("EarningTypeName should not be more than 30 Char")
        return value

