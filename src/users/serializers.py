
from django.contrib.auth.models import  Group
from rest_framework import serializers
from users.models import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin, NestedCreateMixin, NestedUpdateMixin
from rest_framework.validators import UniqueTogetherValidator
from api.serializers.system import EmployeeSerializer

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('pk', 'apartment', 'street', 'city', 'state', 'country',
                  'state', 'country', 'postCode', 'zipCode')


class UserSerializer( WritableNestedModelSerializer):
    # Reverse OneToOne relation
    employee_details = EmployeeSerializer(required=False)
    address= AddressSerializer(required=False)

    phone = serializers.CharField(max_length=20)
    customer_details = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = UserModel
        fields = ('pk','username', 'email', 'first_name', 'last_name', 'other_name', 'gender', 'phone', 'photo_url', 'bio',"uAccountType", "address", "customer_details", "employee_details" )
        read_only_fields = ('email', )
        validators = [
            UniqueTogetherValidator(
                queryset=UserModel.objects.all(),
                fields=('phone',)
            )
        ]

class UserDetailsSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=20, required=True)
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'phone', 'first_name', 'last_name', )
        read_only_fields = ('email', )
        validators = [
            UniqueTogetherValidator(
                queryset=UserModel.objects.all(),
                fields=('phone',)
            )
        ]


class UserDocumentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = UserDocument
        fields = ('pk', 'name', 'file_hash', 'purpose', 'url', 'owner')
        depth = 1

    def create(self, validated_data):
        return UserDocument.objects.create(owner=get_current_authenticated_user(), **validated_data)

        


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
