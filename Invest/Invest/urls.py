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
    path('account/', include('account.urls')),
    path('', include('dashboard.urls')),
    path('', include('messanger.urls')),
    path('notifications/', include('notifications.urls')),
    path('pay_services/', include('pay_services.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # add root static files
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
