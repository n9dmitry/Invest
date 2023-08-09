"""
    Invest URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('item.urls')),
    path('accounts/', include('account.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('messanger/', include('messanger.urls')),
    path('notifications/', include('notifications.urls')),
    path('pay_services/', include('pay_services.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
