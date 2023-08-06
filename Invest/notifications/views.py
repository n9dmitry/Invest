"""
    Представления для приложения с Уведомлениями
"""

from django.shortcuts import render

# Create your views here.


def notifications(request):
    """
        Показывает уведомления которые есть на аккаунте
    """
    return render(request, 'notifications/notifications.html')
