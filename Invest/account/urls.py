from django.urls import path
# pylint: disable=all
from . import views
# pylint: enable=all
from django.conf import settings
from django.conf.urls.static import static
from .views import activate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('my_items', views.my_items, name='my_items'),
    path('favorites/', views.favorites, name='favorite'),
    path('account_panel', views.account_panel, name='account_panel'),
    path('account_settings', views.account_settings, name='account_settings'),
    path('registration', views.signup, name='registration'),
    path('add_favorite/', views.add_to_favorite, name='add_favorite'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',activate, name='activate'), 
    path('authorization', LoginView.as_view(template_name='account/authorization.html'), name='authorization'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('account_review/', views.account_review, name='account_review'),
    path('add_review/', views.add_review, name='add_review'),
    # URL-шаблон для отправки электронной почты с инструкциями по восстановлению пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    # URL-шаблон для страницы подтверждения восстановления пароля
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
       name='password_reset_confirm'),
    # URL-шаблон для страницы успешного завершения восстановления пароля
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(),
       name='password_reset_done'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    