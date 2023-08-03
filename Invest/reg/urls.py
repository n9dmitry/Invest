from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('authorization/',
         views.authorization, name='authorization'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
]