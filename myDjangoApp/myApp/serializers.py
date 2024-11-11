from rest_framework import serializers

class UserAuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
