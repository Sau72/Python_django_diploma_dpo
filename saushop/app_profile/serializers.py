from rest_framework import serializers
from .models import ImageProfile, Profile
from django.contrib.auth.models import User


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProfile
        fields = ["src", "alt"]


class UserSerializer(serializers.ModelSerializer):
    avatar = ImageSerializer()

    class Meta:
        model = Profile
        fields = ["fullName", "email", "phone", "avatar"]


class DataImageUpdateSerializer(serializers.ModelSerializer):
    src = serializers.CharField()
    alt = serializers.CharField()

    class Meta:
        model = ImageProfile
        fields = ["src", "alt"]


class UserUpdateSerializer(serializers.ModelSerializer):
    avatar = DataImageUpdateSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["fullName", "email", "phone", "avatar"]


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255)


class ImageUpdateSerializer(serializers.Serializer):
    avatar = serializers.ImageField()
