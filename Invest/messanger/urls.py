from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.chat, name='chat'),
    path('messenger', views.messenger, name='messenger'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
