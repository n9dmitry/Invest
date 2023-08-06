from django.urls import path
# pylint: disable=all
from . import views
# pylint: enable=all


urlpatterns = [
    path('my_items', views.my_items, name='my_item'),
    path('favorites', views.favorites, name='favorite'),
    path('account_panel', views.account_panel, name='account_panel'),
    path('account_settings', views.account_settings, name='account_settings'),
]
