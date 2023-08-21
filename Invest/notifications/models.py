"""
    Модели для приложения Notifications
"""

from django.db import models


class Notification(models.Model):
    """
        Модель для уведомлений
    """
    date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Notification {self.text}"
