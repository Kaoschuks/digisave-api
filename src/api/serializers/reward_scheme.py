from rest_framework import serializers
from api.models.reward_scheme import *


class RewardSchemeSerializer(serializers.ModelSerializer):
    customers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = RewardScheme
        fields = ('pk','name', 'rewardType', 'methodOfCalc', 'customers')

