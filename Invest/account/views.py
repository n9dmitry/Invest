"""
    Представления для приложения Account
"""

from django.shortcuts import render, redirect
from item.models import Item
from django.http import JsonResponse
from .forms import ItemForm
from account.models import Profile
from .forms import RegistrationForm


def registration(request):

    if request.method == 'GET':
        form = RegistrationForm()

        return render(request, 'registration.html', {'form': form})

    if request.method == 'POST':
        print(request.POST)
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('item')
        else:
            form = RegistrationForm()
            return render(request, 'registration.html', {'error': form.error_messages, 'form': form})


def authorization(request):
    return render(request, 'authorization.html')


def my_items(request):
    """
        Представление показывает все Items на странице
    """
    user_items = Item.objects.filter(user=request.user)
    print(user_items[0].get_count_add_favorite())
    context = {
        'user_items': user_items
    }
    return render(request, 'account/my_items.html', context)


def favorites(request):
    """
        Представление показывает избранные Item пользователя
    """
    profile = Profile.objects.get(user=request.user)
    context = {
        'favorites_items': profile.favorites.all()
    }
    return render(request, 'account/favorites.html', context)


def add_to_favorite(request):
    """
        Вьюха для обработки Ajax запросов на добавление в избранное
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        item = Item.objects.get(id=request.POST.get('item_id'))
        item.count_add_favorite.add(request.user)
        item.save()
        profile = Profile.objects.get(user=request.user)

        profile.favorites.add(item)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


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
