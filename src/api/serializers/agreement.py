
from rest_framework import serializers
from api.models.agreement import *
from users.models import UserModel
from users.serializers import UserSerializer
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
# from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin, NestedCreateMixin, NestedUpdateMixin
from rest_framework.response import Response
from rest_framework import status

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = ('pk', 'isSign', 'signature', 'message')

    def create(self, validated_data):
        agreement = Agreement.objects.create(user=get_current_authenticated_user(), **validated_data)
        return Response(agreement, status.HTTP_201_CREATED)