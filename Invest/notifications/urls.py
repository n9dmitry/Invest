from django.urls import path
from . import views  # pylint: disable=all
# pylint: enable=all
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.notifications, name='notifications'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
