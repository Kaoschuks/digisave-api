from django.shortcuts import render
from rest_framework.decorators import action
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from rest_framework import viewsets
from api.serializers.agreement import *
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from core.mixin import LoggingMixin

class AgreementViewSet(LoggingMixin, viewsets.ModelViewSet): 
    """
    API endpoint to interact with user agreements 
    """
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

    # custom actions
    @action(detail=True, methods=['get'])
    def user_agreements(self, request, pk=None):
        agreements = Agreement.objects.filter(user_id = pk)

        # Check for paginations
        page = self.paginate_queryset(agreements)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(agreements, many=True)
        return Response(serializer.data);



# class UserHistoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update user history
#     """
#     queryset = UserHistory.objects.all()
#     serializer_class = UserHistorySerializer

# class UserDocumentViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update user documents
#     """
#     queryset = UserDocument.objects.all()
#     serializer_class = UserDocumentSerializer

# class AddressViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update user documents
#     """
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer

# class UAccountViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update user documents
#     """
#     queryset = UAccount.objects.all()
#     serializer_class = UAccountSerializer

# class BranchViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update user documents
#     """
#     queryset = Branch.objects.all()
#     serializer_class = BranchSerializer

# class EmployeeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update user documents
#     """
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class WithdrawalSchemeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update WithdrawalScheme
#     """
#     queryset = WithdrawalScheme.objects.all()
#     serializer_class = WithdrawalSchemeSerializer

# class ReportSchemeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update ReportScheme
#     """
#     queryset = ReportScheme.objects.all()
#     serializer_class = ReportSchemeSerializer

# class RewardSchemeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update RewardScheme
#     """
#     queryset = RewardScheme.objects.all()
#     serializer_class = RewardSchemeSerializer

# class InterestSchemeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update InterestScheme
#     """
#     queryset = InterestScheme.objects.all()
#     serializer_class = InterestSchemeSerializer

# class SavingsSchemeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update SavingsScheme
#     """
#     queryset = SavingsScheme.objects.all()
#     serializer_class = SavingsSchemeSerializer

# class CustomerViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update Customer
#     """
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class DAccountViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update DAccount
#     """
#     queryset = DAccount.objects.all()
#     serializer_class = DAccountSerializer

# class InterestHistoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update InterestHistory
#     """
#     queryset = InterestHistory.objects.all()
#     serializer_class = InterestHistorySerializer


# class TransferHistoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update Transfer History
#     """
#     queryset = TransferHistory.objects.all()
#     serializer_class = TransferHistorySerializer

# class DebitHistoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update DebitHistory
#     """
#     queryset = DebitHistory.objects.all()
#     serializer_class = DebitHistorySerializer

# class CreditHistoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update CreditHistory
#     """
#     queryset = CreditHistory.objects.all()
#     serializer_class = CreditHistorySerializer

# class DAccountHistoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update DAccountHistory
#     """
#     queryset = DAccountHistory.objects.all()
#     serializer_class = DAccountHistorySerializer

# class DAccountTransConfirmationViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update DAccountTransConfirmation
#     """
#     queryset = DAccountTransConfirmation.objects.all()
#     serializer_class = DAccountTransConfirmationSerializer

# class DAccountTransVerificationViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update DAccountTransVerification
#     """
#     queryset = DAccountTransVerification.objects.all()
#     serializer_class = DAccountTransVerificationSerializer

# class CreditViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update Credit
#     """
#     queryset = Credit.objects.all()
#     serializer_class = CreditSerializer

# class DebitViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update Debit
#     """
#     queryset = Debit.objects.all()
#     serializer_class = DebitSerializer

# class TransferViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update Transfer
#     """
#     queryset = Transfer.objects.all()
#     serializer_class = TransferSerializer

# class DTransactionViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update DTransaction
#     """
#     queryset = DTransaction.objects.all()
#     serializer_class = DTransactionSerializer

# class DCardHistoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update DCardHistory
#     """
#     queryset = DCardHistory.objects.all()
#     serializer_class = DCardHistorySerializer

# class DAccountCardViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update DAccountCard
#     """
#     queryset = DAccountCard.objects.all()
#     serializer_class = DAccountCardSerializer

# class SavingsPlanViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update SavingsPlan
#     """
#     queryset = SavingsPlan.objects.all()
#     serializer_class = SavingsPlanSerializer

# class FundSourceViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint to set or update FundSource
#     """
#     queryset = FundSource.objects.all()
#     serializer_class = FundSourceSerializer