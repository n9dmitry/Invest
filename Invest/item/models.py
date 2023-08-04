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
    parent_category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)


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
    """
        Модель для статистики объявления
    """
    item_id = models.OneToOneField(Item, on_delete=models.CASCADE)
    count_view = models.IntegerField()
    count_phone_number = models.IntegerField()

    def __str__(self):
        return str(f"ItemStatistics {self.id}")


def save_image(instance, filename):
    return '/'.join([str(instance.id), filename])


class ItemImage(models.Model):
    """
        Модель для картинок объявлений
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=save_image, blank=True, null=True)
