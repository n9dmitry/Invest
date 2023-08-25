"""
    Модели для приложения Account
"""

from django.db import models
from django.contrib.auth.models import User
from item.models import Item
from datetime import datetime
from datetime import timedelta
import pytz

class SupportMail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

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
    favorites = models.ManyToManyField(Item, blank=True, null=True)
    snils = models.ImageField(upload_to=save_image, blank=True, null=True)
    passport = models.ImageField(upload_to=save_image, blank=True, null=True)
    ogrn = models.ImageField(upload_to=save_image, blank=True, null=True)
    inn = models.ImageField(upload_to=save_image, blank=True, null=True)
    last_acivity = models.DateTimeField(default=datetime.now())

    def user_is_online(self):
        past_time_with_timezone = (
            datetime.now()-timedelta(minutes=5)).replace(tzinfo=pytz.UTC)
        print('PAST: ', str(past_time_with_timezone))
        print('last: ', str(self.last_acivity))
        if self.last_acivity <= past_time_with_timezone:
            return False
        return True

    def __str__(self):
        # pylint: disable=all
        return self.user.email
        # pylint: enable=all
