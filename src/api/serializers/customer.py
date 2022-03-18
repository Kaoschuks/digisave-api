from rest_framework import serializers
from api.models.customer import *
from users.serializers import UserSerializer
from api.serializers.daccount import DAccountSerializer
from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin, NestedCreateMixin, NestedUpdateMixin


class CustomerSerializer(WritableNestedModelSerializer):
    user = UserSerializer(read_only=True)
    rewards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    accounts = DAccountSerializer(many=True,read_only=True)
    class Meta:
        model = Customer
        fields = ('pk','home_phone', 'emergency_phone', 'creator','user', 'rewards', 'accounts')
