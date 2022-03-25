from rest_framework import serializers
from multi_emails.models import SendEmail


class SendEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmail
        fields = ('id', 'message', 'recipient')

