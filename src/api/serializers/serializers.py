
from rest_framework import serializers


# class InterestHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InterestHistory
#         fields = ('message', )


# class TransferHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TransferHistory
#         fields = ('message', )


# class DebitHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DebitHistory
#         fields = ('message', )


# class CreditHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CreditHistory
#         fields = ('message', )


# class DAccountHistorySerializer(serializers.ModelSerializer):
#     interestHistory = InterestHistorySerializer()
#     transferHistory = TransferHistorySerializer()
#     debitHistory = DebitHistorySerializer()
#     creditHistory = CreditHistorySerializer()

#     class Meta:
#         model = DAccountHistory
#         fields = ('interestHistory', 'transferHistory', "debitHistory",
#                   "creditHistory")

#     def create(self, validated_data):
#         interestHistory = validated_data.pop('interestHistory')
#         transferHistory = validated_data.pop('transferHistory')
#         debitHistory = validated_data.pop('debitHistory')
#         creditHistory = validated_data.pop('creditHistory')

#         history = DAccountHistory.objects.create(**validated_data)
#         if (interestHistory.is_valid()):
#             interestHistory.objects.create(history, **interestHistory)
#         if (transferHistory.is_valid()):
#             transferHistory.objects.create(history, **transferHistory)
#         if (debitHistory.is_valid()):
#             debitHistory.objects.create(history, **debitHistory)
#         if (creditHistory.is_valid()):
#             creditHistory.objects.create(history, **creditHistory)
#         return history


# class DAccountTransConfirmationSerializer(serializers.ModelSerializer):
#     transaction = 'DTransactionSerializer'

#     class Meta:
#         model = DAccountTransConfirmation
#         fields = ('initiatedTime', 'abortionTime', 'isConfirmed')
#         read_only_fields = ('DTransactionSerializer', )


# class DAccountTransVerificationSerializer(serializers.ModelSerializer):
#     transaction = 'DTransactionSerializer'

#     class Meta:
#         model = DAccountTransVerification
#         fields = ('message', 'isVerified')
#         read_only_fields = ('DTransactionSerializer', )


# class CreditSerializer(serializers.ModelSerializer):
#     transaction = 'DTransactionSerializer'

#     class Meta:
#         model = Credit
#         fields = ('amount', )
#         read_only_fields = ('DTransactionSerializer', )


# class DebitSerializer(serializers.ModelSerializer):
#     transaction = 'DTransactionSerializer'

#     class Meta:
#         model = Debit
#         fields = ('amount', )
#         read_only_fields = ('DTransactionSerializer', )


# class TransferSerializer(serializers.ModelSerializer):
#     transaction = 'DTransactionSerializer'

#     class Meta:
#         model = Transfer
#         fields = ('amount', )
#         read_only_fields = ('DTransactionSerializer', )


# class DTransactionSerializer(serializers.ModelSerializer):
#     initiator = EmployeeSerializer(read_only=True)
#     confirmation = DAccountTransConfirmationSerializer()
#     verification = DAccountTransVerificationSerializer()
#     debit = DebitSerializer()
#     credit = CreditSerializer()
#     transfer = TransferSerializer()

#     class Meta:
#         model = DTransaction
#         fields = ('id', 'initiator', 'confirmation', "verification", 'debit',
#                   'credit', 'transfer')

#     def create(self, validated_data):
#         confirmation = validated_data.pop('confirmation')
#         verification = validated_data.pop('verification')
#         debit = validated_data.pop('debit')
#         credit = validated_data.pop('credit')

#         transaction = DTransaction.objects.create(**validated_data)
#         if (confirmation.is_valid()):
#             confirmation.objects.create(transaction, **confirmation)
#         if (verification.is_valid()):
#             verification.objects.create(transaction, **verification)
#         if (debit.is_valid()):
#             debit.objects.create(transaction, **debit)
#         if (credit.is_valid()):
#             credit.objects.create(transaction, **credit)

#         return transaction


# class DCardHistorySerializer(serializers.ModelSerializer):
#     card = "DAccountCardSerializer"

#     class Meta:
#         model = DCardHistory
#         fields = ('message', "dateCreated", 'card')
#         read_only_field = ('card', )


# class DAccountCardSerializer(serializers.ModelSerializer):
#     history = DCardHistorySerializer()
#     accountHolder = CustomerSerializer(read_only=True)
#     linkedAccount = DAccountSerializer(read_only=True)
#     transaction = DTransactionSerializer()

#     class Meta:
#         model = DAccountCard
#         fields = ('cardType', 'lastUsed', 'history', 'accountHolder',
#                   'linkedAccount', 'transaction')


