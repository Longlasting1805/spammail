from rest_framework import serializers


class Login_serializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class Register_serializer(serializers.ModelSerializer):
    class Meta:
        email = serializers.EmailField()
        name = serializers.CharField()
