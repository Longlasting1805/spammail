from django.contrib import admin
from .models import CustomUserManager, Custom_user

# admin.site.register(CustomUserManager)
admin.site.register(Custom_user)
# Register your models here.
