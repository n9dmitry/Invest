from django.urls import path
# так вьюхи незя импортировать
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.all_items, name='all_items'),
                  path('iteminfo/<int:item_id>/', views.iteminfo, name='iteminfo'),
                  path('additem', views.additem, name='additem'),
                  path('edit_item/<int:item_id>', views.edit_item, name='edit_item'),
                  path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
                  path('about/', views.about, name='about'),
                  path('support/', views.support, name='support'),
                  path('increment_count_phone_number_item/', views.increment_count_phone_number_item,
                       name='increment_count_phone_number_item'),
                  path('iteminfo/<int:item_id>/add_review/', views.CreateReview.as_view(), name='add_review'),
                  path('my_reviews/', views.my_reviews, name='my_reviews'),
                  path('my_reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review'),
                  path('rev_delete/<int:pk>/', views.review_delete, name = 'del_review'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
