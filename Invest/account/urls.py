from django.urls import path
# pylint: disable=all
from . import views
# pylint: enable=all
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('my_items', views.my_items, name='my_items'),
    path('favorites/', views.favorites, name='favorite'),
    path('account_panel', views.account_panel, name='account_panel'),
    path('account_settings', views.account_settings, name='account_settings'),
    path('registration', views.registration, name='registration'),
    path('authorization', views.authorization, name='authorization'),
    path('add_favorite/', views.add_to_favorite, name='add_favorite')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
