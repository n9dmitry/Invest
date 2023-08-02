from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interest = models.CharField(max_length=255)
    avatar_path = models.CharField(max_length=255)
    profile_info = models.TextField()
    phone_number = models.CharField(max_length=20)
    phone_verified = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


