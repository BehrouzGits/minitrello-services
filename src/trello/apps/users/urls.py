from django.urls import path

from .view import OTPView


urlpatterns = [
    path('otp', OTPView.as_view(), name = 'otp_view')
]