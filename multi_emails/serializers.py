from rest_framework import serializers
from multi_emails.models import send_multi_email


class send_email_serializer(serializers.ModelSerializer):
    class Meta:
        model = send_multi_email
        fields = ('id', 'message', 'recipient')

