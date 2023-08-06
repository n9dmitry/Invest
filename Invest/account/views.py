"""
    Представления для приложения Account
"""

from django.shortcuts import render


def my_items(request):
    """
        Представление показывает все Items на странице
    """
    return render(request, 'account/my_items.html')


def favorites(request):
    """
        Представление показывает избранные Item
    """
    return render(request, 'account/favorites.html')


def account_panel(request):
    """
        Панель действий связанных с аккаунтом
    """
    return render(request, 'account/account_tempalte_panel.html')


def account_settings(request):
    """
        Показывает настройки аккаунта
    """
    return render(request, 'account/account_settings.html')
