from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    city = models.CharField(max_length=255)
    required_investment = models.CharField(max_length=255)
    profit_per_month = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserFavoriteItem(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    user_id = models.IntegerField()

    def __str__(self):
        return f"UserFavoriteItem {self.id}"

class ItemImage(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"ItemImage {self.id}"

class ItemStatistics(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    count_view = models.IntegerField()
    count_phone_number = models.IntegerField()

    def __str__(self):
        return f"ItemStatistics {self.id}"

class ItemCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    item_id = models.IntegerField()
    parent_category_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"ItemCategory {self.id}"

