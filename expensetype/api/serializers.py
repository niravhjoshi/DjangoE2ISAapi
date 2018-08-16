from rest_framework import serializers
import datetime
from expensetype.models import ExpenseType

class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType
        fields = [
            'U_id',
            'ExpenseType_id',
            'ExpenseTypeName',
            'ExpenseType_CDate'
        ]


    def validate_expensetype(self,value):
        if len(value) > 30:
            raise serializers.ValidationError("ExpenseTypeName should not be more than 30 Char")
        return value

