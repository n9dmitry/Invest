from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Message {self.id}"


class Notification(models.Model):
    date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Notification {self.id}"
