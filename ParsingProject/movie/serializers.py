from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.Serializer):
    url = serializers.ListField(child=serializers.CharField(max_length=200))


