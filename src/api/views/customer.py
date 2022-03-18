# from django.shortcuts import render
from rest_framework.decorators import action
# from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from rest_framework import viewsets
from api.models.customer import Customer
from api.serializers.customer import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from core.mixin import LoggingMixin
from users.models import UserModel
from django.shortcuts import get_object_or_404


class CustomerViewSet(LoggingMixin,viewsets.ModelViewSet):
    """
    API endpoint to set or update Customer. Note: Use create_customer other than the normal create function
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['post', 'put'])
    def create_customer(self, request, pk=None):
        """
        Create new customer for the user with the pk provided
        """
        customer = CustomerSerializer(data=request.data)
        customer.is_valid(raise_exception=True)
        user =  get_object_or_404(UserModel, pk=pk,)
        if user is not None:
            # Customer already exist
            if hasattr(user, 'client') and user.client is not None:
                 return Response({"status":"user is a customer"}, status.HTTP_304_NOT_MODIFIED)
            user.uAccountType = "CUSTOMER"
            user.save()
            customer.save(user=user)
            return Response(customer.data, status.HTTP_200_OK)
        else:
            Response({"status":"user not found"}, status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def get_customer(self, request, pk=None):
        """
        Fetch customer with the  user pk provided. Note: pk should be user id not customer id
        """
        user =  get_object_or_404(UserModel, pk=pk,)
        print(user)
        if user is not None:
                # Customer already exist
            if hasattr(user, 'client') and user.client is not None:
                customer = get_object_or_404(self.queryset, pk=user.client.pk)
                customer = CustomerSerializer(instance=customer)
                # customer.is_valid(raise_exception=True)
                return Response(customer.data, status.HTTP_200_OK)
        return Response({"status":"User is not a customer"}, status.HTTP_404_NOT_FOUND)

    def create(self, request, pk=None):
            return  Response({"status":"Use /api/customer/{id}/create_customer instead"},status.HTTP_403_FORBIDDEN)

