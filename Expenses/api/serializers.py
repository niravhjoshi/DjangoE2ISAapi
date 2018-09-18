from rest_framework import serializers
import datetime
from Expenses.models import ExpensesEntry
from persons.models import Person
from expensetype.models import ExpenseType


class ExpensesSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(ExpensesSerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['PersonName'].queryset = Person.objects.filter(UserName=request_user)
        self.fields['Exp_Type_Name'].queryset = ExpenseType.objects.filter(UserName=request_user)
    class Meta:
        model = ExpensesEntry
        fields = [
            'ExpensesId',
            'UserName',
            'PersonName',
            'Exp_Type_Name',
            'Exp_Amt',
            'Exp_Img',
            'Exp_date',
            'Exp_comm'
        ]
        read_only_fields=['UserName'] # Get calls its gone be read only.


    def validate_exp_date(self, value):
        if datetime.datetime.strptime(value, '%Y-%m-%d'):
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD")
        return value


