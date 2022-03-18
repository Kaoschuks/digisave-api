from rest_framework import serializers
from api.models.report_scheme import ReportScheme

class ReportSchemeSerializer(serializers.ModelSerializer):
    accounts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ReportScheme
        fields = ('pk','name', 'show_accountId', 'show_accountType', 'show_planType',
                  'show_accountHolder', 'show_transactions', 'show_currentBalance',
                  'show_interestScheme', 'show_aim', 'genFrequency', 'dateCreated', 'accounts')

