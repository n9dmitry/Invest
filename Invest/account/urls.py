from django.urls import path
from . import views

urlpatterns = [
    path('chat', views.chat, name='chat'),
    path('messenger', views.messenger, name='messenger'),
    path('my_item', views.my_item, name='my_item'),
    path('favorite', views.favorite, name='favorite'),
    path('base_panel', views.base_panel, name='base_panel'),
    path('notifications', views.notifications, name='notifications'),
    path('pay_services', views.pay_services, name='pay_services'),
    path('account_settings', views.account_settings, name='account_settings'),
]