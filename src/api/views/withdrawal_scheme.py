from rest_framework import serializers
from api.models.withdrawal_scheme import WithdrawalScheme
from api.models.daccount  import DAccount
from api.serializers.daccount import WithdrawalSchemeSerializer, DAccountSerializer
from rest_framework import viewsets
from core.mixin import LoggingMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action


class WithdrawalSchemeViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to Manage WithdrawalScheme, apply scheme to account 
    to control withdrawals based on the policy
    """
    queryset = WithdrawalScheme.objects.all()
    serializer_class = WithdrawalSchemeSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("name", "totalAllowedWithdrawals", "maxAmountAllowed")
    # permission_classes = (myapp.permissions.CustomObjectPermissions,)

    @action(detail=True, methods=['get'])
    def accounts(self, request, pk=None):
        """
        Get all accounts registered to to the withdrawal policy
        """
        # try:
        #     customer_id = request.data["customer_id"].strip()
        #     scheme_id = request.data["scheme_id"].strip()
        #     int(customer_id)
        #     int(scheme_id)
        # except: 
        #     return Response({"status":"Invalid pk"}, status.HTTP_400_BAD_REQUEST)

        # if not scheme_id:
        #     return Response({"status":"Scheme id cannot be empty"}, status.HTTP_400_BAD_REQUEST)
        # if not customer_id:
        #     return Response({"status":"Customer id cannot be empty"}, status.HTTP_400_BAD_REQUEST)
        
        policy = get_object_or_404(self.queryset, pk=pk)
        policy_s = WithdrawalSchemeSerializer(instance=policy)
        account_keys = policy_s.data["withdrawal_account"]
        accounts = []
        for key in account_keys:
            accounts.append(DAccountSerializer(instance=get_object_or_404(DAccount, pk=key)).data)
        return Response(accounts, status.HTTP_200_OK)


    # Don't allow deletion of policy in used by an account
    def destroy(self, request, pk=None):
            # get the reward_object 
        if self.queryset is None:
            return Response(status.HTTP_404_NOT_FOUND)

        policy = get_object_or_404(self.queryset, pk=pk)
        policy_s = WithdrawalSchemeSerializer(instance=policy)
    
        # check if no one is on the scheme 
        if len(policy_s.data["withdrawal_account"])>0:
            return Response({"status":"There are accounts using the scheme"}, status.HTTP_403_FORBIDDEN)
        
        policy.delete()
        return Response(status.HTTP_200_OK)