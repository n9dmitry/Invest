"""
    Представления для приложения с Уведомлениями
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def notifications(request):
    """
        Показывает уведомления которые есть на аккаунте
    """
    return render(request, 'notifications/notifications.html')
