# from django.shortcuts import render
from rest_framework.decorators import action
# from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from rest_framework import viewsets
from api.serializers.reward_scheme import RewardSchemeSerializer
from api.models.reward_scheme import RewardScheme
from rest_framework import status
from rest_framework.response import Response
#   om django.http import Http404
from core.mixin import LoggingMixin
from rest_auth import serializers
from django.shortcuts import get_object_or_404
from api.serializers.customer import *

class RewardSchemeViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to set or update RewardScheme
    """
    queryset = RewardScheme.objects.all()
    serializer_class = RewardSchemeSerializer

    @action(detail=False, methods=['post'])
    def add_customer(self, request ):
        """
        Add a customer to a reward scheme, pk is customer id, and data is {"customer_id":"2","scheme_id": ""}
        """
        try:
            customer_id = request.data["customer_id"].strip()
            scheme_id = request.data["scheme_id"].strip()
            int(customer_id)
            int(scheme_id)
        except: 
            return Response({"status":"Invalid pk"}, status.HTTP_400_BAD_REQUEST)

        if not scheme_id:
            return Response({"status":"Scheme id cannot be empty"}, status.HTTP_400_BAD_REQUEST)
        if not customer_id:
            return Response({"status":"Customer id cannot be empty"}, status.HTTP_400_BAD_REQUEST)
        
        customer = get_object_or_404(Customer, pk=customer_id)
        rewardScheme = get_object_or_404(self.queryset, pk=scheme_id)
        rewardScheme.customers.add(customer)
        rewardScheme.save()
        rewardScheme = RewardSchemeSerializer(instance=rewardScheme)
        return Response(rewardScheme.data, status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def remove_customer(self, request, pk=None):
        """
        remove a customer from a reward scheme, pk is customer id, and data is {reward_id: id}
        """
        try:
            customer_id = request.data["customer_id"].strip()
            scheme_id = request.data["scheme_id"].strip()
            int(customer_id)
            int(scheme_id)
        except: 
            return Response({"status":"Invalid pk"}, status.HTTP_400_BAD_REQUEST)

        if not scheme_id:
            return Response({"status":"Scheme id cannot be empty"}, status.HTTP_400_BAD_REQUEST)
        if not customer_id:
            return Response({"status":"Customer id cannot be empty"}, status.HTTP_400_BAD_REQUEST)
          
        customer = get_object_or_404(Customer, pk=customer_id)
        rewardScheme = get_object_or_404(self.queryset, pk=scheme_id)

        rewardScheme.customers.remove(customer)
        rewardScheme.save()
        rewardScheme = RewardSchemeSerializer(instance=rewardScheme)
        return Response(rewardScheme.data, status.HTTP_200_OK)



    def destroy(self, request, pk=None):
        # get the reward_object 
        if self.queryset is None:
            return Response(status.HTTP_404_NOT_FOUND)

        reward = get_object_or_404(self.queryset, pk=pk)
        reward_s = RewardSchemeSerializer(instance=reward)
    
        # check if no one is on the scheme 
        if len(reward_s.data["customers"])>0:
            return Response({"status":"There are customers using the scheme"}, status.HTTP_403_FORBIDDEN)
        
        reward.delete()
        return Response(status.HTTP_200_OK)