from rest_framework import serializers
from api.models.daccount import DAccount
from api.models.customer import Customer
from api.models.withdrawal_scheme import WithdrawalScheme
from api.serializers.report_scheme import ReportSchemeSerializer
from api.models.report_scheme import ReportScheme
# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.response import Response
from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin, NestedCreateMixin, NestedUpdateMixin



class DAccountSerializer(WritableNestedModelSerializer):
    # reports = ReportSchemeSerializer(many=True, required=False)
    customer_id = serializers.IntegerField()
    withdrawalScheme_id =  serializers.IntegerField()
    # branch = BranchSerializer(read_only=True)
    # report_schemes = ReportSchemeSerializer(many=True,required=False)
    report_schemes = serializers.PrimaryKeyRelatedField(queryset=ReportScheme.objects.all(), many=True, required=False)
    # history = 'DAccountHistorySerializer'

    class Meta:
        model = DAccount
        fields = ("pk",'accountNumber', 'balance', 'amountWithdrawable',
                  'freeWithdrawalBalance', 'lockUpPeriod',
                  'status', 'accountType', 'dateCreated', 'createdBy','customer_id',"withdrawalScheme_id",
                   "report_schemes")
        read_only_fields = ('history', 'createdBy', 'dateCreated')


class WithdrawalSchemeSerializer(serializers.ModelSerializer):
    withdrawal_account = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = WithdrawalScheme
        fields = ("pk",'name', 'totalAllowedWithdrawals',
                  'allowedDates', 'penaltyRate', 'maxAmountAllowed', 'emergencyAllowedWithdrawals',
                  'withdrawalInterval',"withdrawalIntervalUnit", "createdBy", "withdrawal_account")
