from django.urls import path
from . import views

urlpatterns = [
    path('dashboard_auth/', views.enter, name='dashboard_enter'),
    path('dashboard/', views.dashboard, name='dashboard_main'),
]