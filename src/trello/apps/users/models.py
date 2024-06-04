import random
import string
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from trello.apps.users.sender import send_otp

# Create your models here.

class User(AbstractUser):
    pass

class OtpRequestQuerySet(models.QuerySet):
    def is_valid(self, receiver, request, password):
        return self.filter(
            receiver=receiver,
            request_id=request,
            password=password
        ).exists()


class OTPManager(models.Manager):

    def get_queryset(self):
        return OtpRequestQuerySet(self.model, self._db)
    
    def generate(self, data):
        otp =self.model(channel=data['channel'], receiver=data['receiver'])
        otp.save(using=self._db)
        send_otp(otp)
        return otp


def generate_otp():
    rand = random.SystemRandom()
    digits = rand.choices(string.digits, k=4)
    return ''.join(digits)


class OTPRequest(models.Model):
    class OtpChannel(models.TextChoices):
        PHONE = 'Phone'
        EMAIL = 'E-Mail'
    request_id = models.UUIDField(primary_key=True, editable=False, default= uuid.uuid4)
    channel = models.CharField(max_length=10, choices=OtpChannel.choices, default=OtpChannel.PHONE)
    receiver = models.CharField(max_length=50)
    password = models.CharField(max_length=4, default=generate_otp)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    objects = OTPManager()