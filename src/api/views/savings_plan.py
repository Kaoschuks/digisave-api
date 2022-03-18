from api.models.savings_plan import (SavingsPlan, SavingsScheme, Aim, FundSource, 
InterestScheme)
# from api.models.daccount import DAccount
# from api.serializers.daccount import DAccountSerializer
from api.serializers.savings_plan import (SavingsPlanSerializer, FundSourceSerializer,SavingsSchemeSerializer, AimSerializer,
InterestSchemeSerializer)

from rest_framework import viewsets
from core.mixin import LoggingMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend


class SavingsSchemeViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to set or update SavingsScheme
    """
    queryset = SavingsScheme.objects.all()
    serializer_class = SavingsSchemeSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'miniPrincipal', 'minLumpsum', 'miniPrincipal', 'allowedCurrencies', 'minLumpsum', 'savingsType',
                  'savingsFrequency', 'allowSwiftSave', 'allowESave','allowMultiple', 'allowInterest', 'minimumInvestPeriod', 
                  'minimumInvestPeriodUnit')
    # permission_classes = (myapp.permissions.CustomObjectPermissions,)
    
    # Don't allow deletion of policy in used by an account
    def destroy(self, request, pk=None):
            # get the reward_object 
        if self.queryset is None:
            return Response(status.HTTP_404_NOT_FOUND)

        policy = get_object_or_404(self.queryset, pk=pk)
        policy_s = SavingsSchemeSerializer(instance=policy)
    
        # check if no one is on the scheme 
        if len(policy_s.data["scheme_plan"])>0:
            return Response({"status":"There are savings-plan using the scheme"}, status.HTTP_403_FORBIDDEN)
        policy.delete()
        return Response(status.HTTP_200_OK)


class SavingsPlanViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to set or update SavingsPlan
    """
    queryset = SavingsPlan.objects.all()
    serializer_class = SavingsPlanSerializer
    filter_backends = (DjangoFilterBackend,)

    filterset_fields = ('interestAccred', 'lumpSum')
    # permission_classes = (myapp.permissions.CustomObjectPermissions,)

    # def create(self, request, pk=None):
    #     print(request.data);
    #     plan = SavingsPlanSerializer(data = request.data)
    #     plan.is_valid(raise_exception=True)

    #     return Response(request.data, status.HTTP_200_OK)      

class FundSourceViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to set or update FundSource
    """
    queryset = FundSource.objects.all()
    serializer_class = FundSourceSerializer
    def destroy(self, request, pk=None):
            # get the reward_object 
        
        return Response(status.HTTP_403_FORBIDDEN)



class InterestSchemeViewSet(viewsets.ModelViewSet):
    """
    API endpoint to set or update InterestScheme
    """
    queryset = InterestScheme.objects.all()
    serializer_class = InterestSchemeSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'interestRate', 'interestType', 'frequency')
    # permission_classes = (myapp.permissions.CustomObjectPermissions,)

    def destroy(self, request, pk=None):
            # get the reward_object 
        return Response(status.HTTP_403_FORBIDDEN)

