"""
    Модели для Item
"""
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models

from .tasks import set_avg_rating


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
    required_investment = models.IntegerField(blank=True, null=True)
    profit_per_month = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    images = models.ManyToManyField(
        'ItemImage', related_name='images_for_item')
    contacts = models.CharField(max_length=500, blank=True, null=True)
    count_view = models.IntegerField(default=0)
    count_get_contacts = models.IntegerField(default=0)
    count_add_favorite = models.ManyToManyField(
        User, related_name='favorite_items')
    status = models.CharField(max_length=100, default='Проверяется')
    avg_rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default= 0.0)
    # TODO: надо добавить пункт active
    #  пусть объявления вечно не висят

    def __str__(self):
        return str(self.title)

    def get_count_add_favorite(self):
        return len(self.count_add_favorite.all())


def save_image(instance, filename):
    return '/'.join(['itemimg', str(instance.item_id), filename])


class ItemImage(models.Model):
    """
        Модель для картинок объявлений
    """
    item_id = models.IntegerField(blank=True, null=True)
    image = models.ImageField(
        upload_to=save_image, blank=True, null=True)

class Reviews(models.Model):
    """

    """
    RATING_RANGE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_RANGE)
    text = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(1000)])
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def save(self):
        item_id = self.item.__getattribute__('id')
        print(item_id)
        set_avg_rating.delay(item_id)
        return super().save()

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


def save_rev_images(instance, filename):
    return '/'.join(['revimages', str(instance.image), filename])

class ReviewsImages(models.Model):
    image = models.ImageField(upload_to=save_rev_images)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)

