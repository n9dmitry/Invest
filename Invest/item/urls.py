from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='all_items'),
    path('iteminfo', views.iteminfo, name='iteminfo'),
    path('additem', views.additem, name='additem')

]
