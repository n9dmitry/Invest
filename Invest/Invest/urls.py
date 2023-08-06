"""
    Invest URL Configuration
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reg.urls')),
    path('', include('item.urls')),
    path('accounts', include('account.urls')),
    path('dashboard', include('dashboard.urls')),
    path('messanger', include('messanger.urls')),
    path('notifications', include('notifications.urls')),
    path('pay_services', include('pay_services.urls'))
]
