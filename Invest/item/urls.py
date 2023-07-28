from django.urls import path
from . import views

urlpatterns = [
    path('', views.item, name='item'),
    path('iteminfo', views.iteminfo, name='iteminfo'),
    path('additem', views.additem, name='additem')

]