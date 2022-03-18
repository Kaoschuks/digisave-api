
# from django.shortcuts import render
from rest_framework.decorators import action
# from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from rest_framework import viewsets
from api.serializers.report_scheme import ReportSchemeSerializer
from api.models.report_scheme import ReportScheme
from rest_framework import status
from rest_framework.response import Response
#   om django.http import Http404
from core.mixin import LoggingMixin
from rest_auth import serializers
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class ReportSchemeViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to set or update ReportScheme
    """
    queryset = ReportScheme.objects.all()
    serializer_class = ReportSchemeSerializer
    
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'show_accountId', 'show_accountType', 'show_planType',
                  'show_accountHolder', 'show_transactions', 'show_currentBalance',
                  'show_interestScheme', 'show_aim', 'genFrequency', 'dateCreated')