from rest_framework import serializers
from api.models.savings_plan import (SavingsPlan, SavingsScheme, Aim,
                                     FundSource, InterestScheme, ExternalBank)
from api.serializers.daccount import DAccountSerializer
# from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin, NestedCreateMixin, NestedUpdateMixin


class InterestSchemeSerializer(WritableNestedModelSerializer):
    savings_scheme = serializers.PrimaryKeyRelatedField(many=True,
                                                        read_only=True)

    class Meta:
        model = InterestScheme
        fields = ("pk", 'name', 'interestRate', "interestType", "frequency",
                  "savings_scheme")


class SavingsSchemeSerializer(WritableNestedModelSerializer):
    # scheme_plan = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    interestScheme = InterestSchemeSerializer(required=False)
    class Meta:
        model = SavingsScheme
        fields = ('pk', 'name', 'miniPrincipal', 'allowedCurrencies',
                  'minLumpsum', 'savingsType', 'savingsFrequency',
                  'allowSwiftSave', 'allowESave', 'allowMultiple',
                  'allowInterest', 'minimumInvestPeriod',
                  'minimumInvestPeriodUnit', 'interestScheme')
        depth = 1
        # read_only_fields = ('scheme_plan', )


class AimSerializer(serializers.ModelSerializer):
    aim_plan = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Aim
        fields = ('pk', 'name', 'targetDate', 'calculatedAmount',
                  'savingsFreq', 'aim_plan')


class ExternalBankSerializer(WritableNestedModelSerializer ):
    fundSource = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ExternalBank
        fields = ('pk', 'accountName', 'accountNumber', 'accountType',
                  'allowedUSSDTrans', 'allowedPhoneTrans', 'bankName',
                  'bankId', 'secreteToken', 'fundSource')


class FundSourceSerializer(WritableNestedModelSerializer):
    bank = ExternalBankSerializer(required=False)
    # plan = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = FundSource
        fields = ('pk', 'sourceType', 'info','bank')


class SavingsPlanSerializer(WritableNestedModelSerializer):
    savingsScheme = SavingsSchemeSerializer(required=False)
    savingsScheme_id = serializers.IntegerField()
    account = DAccountSerializer(required=False)
    account_id = serializers.IntegerField()
    aim = AimSerializer(required=False)
    plan_fundSource = FundSourceSerializer(many=True)

    class Meta:
        model = SavingsPlan
        fields = ('pk', 'interestAccred', 'lumpSum', 'account', 'account_id','savingsScheme', 'savingsScheme_id',
                  'aim', 'plan_fundSource')
        depth=2

    # def create(self, validated_data):
    #     # account = validated_data.pop('account')
    #     # aim = validated_data.pop('aim')
    #     # fundSource = validated_data.pop('fundSource')
    #     # plan = SavingsPlan.objects.create(**validated_data)
    #     # if (account.is_valid()):
    #     #     account.objects.create(plan, **account)
    #     # if (aim.is_valid()):
    #     #     aim.objects.create(plan, **aim)
    #     # if (fundSource.is_valid()):
    #     #     fundSource.objects.create(plan, **fundSource)
    #     print(validated_data)
    #     return Response(validated_data, status.HTTP_200_OK)
