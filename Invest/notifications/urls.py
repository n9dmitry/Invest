from django.urls import path
from . import views  # pylint: disable=all
# pylint: enable=all

urlpatterns = [
    path('notifications', views.notifications, name='notifications'),
]
