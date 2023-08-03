from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
        Профиль для пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interest = models.CharField(max_length=50)
    avatar = models.ImageField(blank=True, null=True)
    profile_info = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    phone_verified = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
