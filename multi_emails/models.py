from django.db import models


class send_multi_email(models.Model):
    message = models.CharField(max_length=500, null=True, blank=True)
    recipient = models.EmailField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.message
# Create your models here.
