from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.all_items, name='all_items'),
    path('iteminfo/<int:item_id>', views.iteminfo, name='iteminfo'),
    path('additem', views.additem, name='additem'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
    path('increment_count_phone_number_item/', views.increment_count_phone_number_item,
         name='increment_count_phone_number_item')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
