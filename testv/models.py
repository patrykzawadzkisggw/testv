from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    folder = models.CharField(max_length=255)

class TrustedDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255)
    device_id = models.CharField(max_length=255)

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_date = models.DateTimeField(auto_now_add=True)
    service = models.CharField(max_length=255)
    encrypted_login = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
