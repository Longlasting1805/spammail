from rest_framework import serializers
from user.models import Custom_user


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_user
        fields = ('id', 'email', 'name', 'created_at', 'updated_at', 'is_staff', 'is_superuser', 'is_active')
