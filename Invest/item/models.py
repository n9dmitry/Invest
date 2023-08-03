"""
    Модели для Item
"""

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """
        Категория для объявления
    """
    title = models.CharField(max_length=220)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE)


class Item(models.Model):
    """
        Проект от пользователя
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255, blank=True, null=True)
    required_investment = models.IntegerField()
    profit_per_month = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.title)


class ItemStatistics(models.Model):
    item_id = models.IntegerField()
    count_view = models.IntegerField()
    count_phone_number = models.IntegerField()

    def __str__(self):
        return f"ItemStatistics {self.id}"
