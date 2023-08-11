"""
    Модели для приложения Account
"""

from django.db import models
from django.contrib.auth.models import User
from item.models import Item


def save_image(instance, filename):
    return '/'.join(['users_avatars', str(instance.user.id), filename])

class Profile(models.Model):
    """
        Профиль для пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interest = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=save_image, blank=True, null=True)
    profile_info = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    phone_verified = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    favorites = models.ManyToManyField(Item)
    snils = models.ImageField(upload_to=save_image, blank=True, null=True)
    passport = models.ImageField(upload_to=save_image, blank=True, null=True)
    ogrn = models.ImageField(upload_to=save_image, blank=True, null=True)
    inn = models.ImageField(upload_to=save_image, blank=True, null=True)
    
    def __str__(self):
        # pylint: disable=all
        return self.user.email
        # pylint: enable=all
