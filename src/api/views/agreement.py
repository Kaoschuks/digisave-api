from django.shortcuts import render
from rest_framework.decorators import action
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from rest_framework import viewsets
from api.serializers.agreement import *
from rest_framework.response import Response
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

