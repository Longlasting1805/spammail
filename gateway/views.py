from django.shortcuts import render
import jwt
from .models import Jwt
from user.models import Custom_user
from datetime import datetime, timedelta
from django.conf import settings
import random
import string
from rest_framework.views import APIView
from rest_framework import mixins, viewsets, permissions
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate


def get_random_data(length):
    ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def get_access_token(payload):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), **payload},
        settings.SECURITY_KEY,
        algorithm="HS256"
    )


def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data": {10}},
        settings.SECURITY_KEY,
        algorithm="HS256"

    )


class LoginView(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = Jwt.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['Email'],
            password=serializer.validated_data['password'])

        if not user:
            return Response({"error": "invalid email or password"}, status=400)

        access = get_access_token({user.id})
        refresh = get_refresh_token()

        Jwt.objects.create(
            user_id=user.id, access=access, refresh=refresh
        )

        return Response({"access": access, "refresh": refresh})


class RegisterView(viewsets.ModelViewSet):

    serializer_class = RegisterSerializer
    queryset = Jwt.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.queryset.filter(owner=self.request.user)
        return user

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        Custom_user.objects.create(**serializer.validated_data)

        return Response({"success": "user created. "})
