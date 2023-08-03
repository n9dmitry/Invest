from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Message {self.id}"


class MessageUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    sender_id = models.IntegerField()
    recipient_id = models.IntegerField()

    def __str__(self):
        return f"MessageUsers {self.id}"


class Notification(models.Model):
    date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Notification {self.id}"


class UserNotification(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=255)

    def __str__(self):
        return f"UserNotification {self.id}"
