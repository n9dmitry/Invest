from django.contrib import admin

from .models import Item, Category, ItemImage, Reviews, ReviewsImages

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(ItemImage)
admin.site.register(Reviews)
admin.site.register(ReviewsImages)