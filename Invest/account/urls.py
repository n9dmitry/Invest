from django.urls import path
from . import views

urlpatterns = [
    path('chat', views.chat, name='chat'),
    path('my_a', views.my_a, name='my_a'),
    path('favorite', views.favorite, name='favorite'),
    path('base_panel', views.base_panel, name='base_panel'),
]