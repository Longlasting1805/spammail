from django.shortcuts import render
from .serializers import custom_user_serializer
from rest_framework import viewsets
from .models import Custom_user


class custom_user_view(viewsets.ModelViewSet):
    serializer_class = custom_user_serializer
    queryset = Custom_user.objects.all()

# Create your views here.
