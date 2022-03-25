from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from .models import Custom_user


class CustomUserView(viewsets.ModelViewSet):
    queryset = Custom_user.objects.all()
    serializer_class = CustomUserSerializer

# Create your views here.
