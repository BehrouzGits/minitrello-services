from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class OTPRequest(models.Model):
    class OtpChannel(models.TextChoices):
        PHONE = 'phone'
        EMAIL = 'E-Mail'
    request_id = models.UUIDField(primary_key=True, editable=False, default= uuid.uuid4)
    channel = models.CharField(max_length=10, choices=OtpChannel.choices, default=OtpChannel.PHONE)
    receiver = models.CharField(max_length=50)
    password = models.CharField(max_length=4)
    created = models.DateTimeField(auto_now_add=True, editable=False)