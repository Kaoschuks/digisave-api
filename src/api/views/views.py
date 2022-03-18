from django.shortcuts import render
from rest_framework.decorators import action
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from rest_framework import viewsets
from api.serializers.agreement import *
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from core.mixin import LoggingMixin



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

