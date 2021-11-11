"""multi_email URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from multi_emails.views import send_email_view
from user.views import custom_user_view
from gateway.views import LoginView, RegisterView

router = routers.DefaultRouter()
router.register(r'gateway_register', RegisterView, basename='Register')
router.register(r'custom_user', custom_user_view, basename='custom_user')
router.register(r'multi_emails', send_email_view, basename='send_emails')
router.register(r'gateways_login', LoginView, basename='login')
urlpatterns = router.urls

# urlpatterns = [
#     url(r'', include(router.urls)),
#     url(r'admin/', include(admin.site.urls), name=admin),
# ]
