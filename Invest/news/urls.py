from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('news/', views.news_list, name='news/news_list'),
    path('dashboard_news/', views.dashboard_news, name='dashboard_news'),
]