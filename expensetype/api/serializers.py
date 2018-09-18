from rest_framework import serializers
import datetime
from expensetype.models import ExpenseType

class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType
        fields = [
            'UserName',
            'ExpenseType_id',
            'ExpenseTypeName',
            'ExpenseType_CDate'
        ]

        read_only_fields = ['UserName']


    def validate_expensetype(self,value):
        if len(value) > 30:
            raise serializers.ValidationError("ExpenseTypeName should not be more than 30 Char")
        return value

