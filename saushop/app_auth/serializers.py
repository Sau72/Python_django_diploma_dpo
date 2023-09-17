from rest_framework import serializers
from django.contrib.auth.models import User


class AuthSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = User
        fields = ("id", "username", "password", "name")
