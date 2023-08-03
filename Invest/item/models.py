"""
    Модели для Item
"""

from django.contrib.auth.models import User
from django.db import models


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
    
    def __str__(self):
        return str(self.title)


class ItemImage(models.Model):
    item_id = models.IntegerField()
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"ItemImage {self.id}"


class ItemStatistics(models.Model):
    item_id = models.IntegerField()
    count_view = models.IntegerField()
    count_phone_number = models.IntegerField()

    def __str__(self):
        return f"ItemStatistics {self.id}"


class ItemCategory(models.Model):
    title = models.CharField(max_length=255)
    item_id = models.IntegerField()
    parent_category_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"ItemCategory {self.id}"
