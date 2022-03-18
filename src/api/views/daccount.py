from api.models.daccount import DAccount
from api.serializers.daccount import DAccountSerializer
from rest_framework import viewsets
from core.mixin import LoggingMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

class DAccountViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to set or update DAccount
    """
    queryset = DAccount.objects.all()
    serializer_class = DAccountSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('accountNumber', 'status', 'accountType', 'createdBy', 'customer_id', 'withdrawalScheme_id')
    # permission_classes = (myapp.permissions.CustomObjectPermissions,)