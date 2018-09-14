from rest_framework import serializers
import datetime
from Shares.models import SharesEntry
from persons.models import Person



class SharesEntrySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(SharesEntrySerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['PersonName'].queryset = Person.objects.filter(UserName=request_user)

    class Meta:
        model = SharesEntry
        fields = [
            'SharesID',
            'UserName',
            'PersonName',
            'Share_Tick_Name',
            'Share_Count',
            'sellTran',
            'Share_Tran_Type',
            'Share_pershare_amt',
            'Share_Buy_Sell_Date',
            'Share_img',
            'Share_comm'

        ]
        read_only_fields=['UserName'] # Get calls its gone be read only.

    def validate_Share_Buy_Sell_Date_date(self, value):
        if datetime.datetime.strptime(value, '%Y-%m-%d'):
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD")
        return value


