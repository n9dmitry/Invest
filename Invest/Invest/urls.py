"""Invest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add item URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add item URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add item URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('reg.urls')),
    path('', include('item.urls')),
    path('', include('account.urls')),
    path('authorization/', views.authorization, name='authorization'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
]
