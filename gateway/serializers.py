from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        email = serializers.EmailField()
        name = serializers.CharField()
