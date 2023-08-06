from django.urls import path
from . import views

urlpatterns = [
    path('pay_services', views.pay_services, name='pay_services'),
]
