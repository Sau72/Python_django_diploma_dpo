from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import (
    UserSerializer,
    PasswordSerializer,
    UserUpdateSerializer,
    ImageUpdateSerializer,
)
from .models import Profile, ImageProfile


class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.filter(user=self.request.user.id).first()
        serializer = UserSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        profile = Profile.objects.filter(user=self.request.user.id).first()
        serializer = UserSerializer(profile)
        return Response(serializer.data)


class ProfileViewUpdate(APIView):
    def post(self, request):
        serializer = UserUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            profile = Profile.objects.filter(user=self.request.user.id).first()

            profile.fullName = serializer.data["fullName"]
            profile.email = serializer.data["email"]
            profile.phone = serializer.data["phone"]

            profile.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)


class ProfilePasswordViewUpdate(APIView):
    def post(self, request):
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # user = User.objects.create(username=username, first_name=name)
            self.request.user.set_password(serializer.data["password"])
            self.request.user.save()
        return Response(serializer.data, status=201)


class ChangeAvatarView(APIView):
    def post(self, request):
        serializer = ImageUpdateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # profile = Profile.objects.filter(user=self.request.user.id).first()
            print(self.request.user.id)
            ImageProfile.objects.filter(alt=self.request.user.id).update_or_create(
                defaults={"src": request.FILES["avatar"]}, alt=self.request.user.id
            )
            return Response(serializer.data, status=200)
        return Response(data=serializer.errors, status=400)
