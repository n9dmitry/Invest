from django.urls import path
from . import views

urlpatterns = [
    path('', views.a, name='a'),
    path('adinfo', views.adinfo, name='adinfo')
]