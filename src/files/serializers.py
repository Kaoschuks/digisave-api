from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
  # pk = serializers.IntegerField(label="ID", required=False)
  class Meta():
    model = File
    fields = ('pk','file', 'purpose', 'timestamp', 'owner')


