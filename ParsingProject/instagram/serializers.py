from rest_framework import serializers

class InstagramSerializer(serializers.Serializer):

    url = serializers.CharField(max_length=200)