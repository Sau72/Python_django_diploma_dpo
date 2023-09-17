from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from app_profile.models import Profile, ImageProfile
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthSerializer


def signIn(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body["username"]
        password = body["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=500)


class signUpView(APIView):
    def post(self, request):
        body = json.loads(request.body)
        serialized = AuthSerializer(data=body)

        if serialized.is_valid():
            username = serialized.data["username"]
            password = serialized.data["password"]
            user = User.objects.create_user(username=username, password=password)
            print(user.id)
            newimg = ImageProfile.objects.create(src="profile/base.jpg", alt=user.id)
            # img = ImageProfile.objects.filter(alt="base").first()
            Profile.objects.create(
                user=user, fullName=serialized.data["name"], avatar=newimg
            )

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response(status=200)
        else:
            return Response(serialized.errors, status=500)
        return Response(status=200)


def signUp_var2(request):
    if request.method == "POST":
        print(request.body)
        body = json.loads(request.body)
        print(body)
        name = body["name"]
        username = body["username"]
        password = body["password"]

        user = User.objects.create(username=username, first_name=name)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, fullName=name)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=500)
    return HttpResponse(status=200)


def signOut(request):
    logout(request)
    return HttpResponse(status=200)
