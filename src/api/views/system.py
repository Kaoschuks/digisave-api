from django.shortcuts import render
from rest_framework.decorators import action
# from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from rest_framework import viewsets
# from rest_framework.response import Response
# from django.http import Http404
# from rest_framework import status
from core.mixin import LoggingMixin
from api.models.system import Branch, Employee
from api.serializers.system import BranchSerializer, EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BranchViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to set or update user documents
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', "location","dateCreated")


class EmployeeViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to set or update user documents
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('workId', 'type', 'employedDate')



 
