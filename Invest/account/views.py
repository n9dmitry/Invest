from django.shortcuts import render

def chat(request):
    return render(request, 'chat.html')

def my_item(request):
    return render(request, 'my_item.html')

def favorite(request):
    return render(request, 'favorite.html')

def base_panel(request):
    return render(request, 'base_panel.html')

def notifications(request):
    return render(request, 'notifications.html')

def pay_services(request):
    return render(request, 'pay_services.html')

def account_settings(request):
    return render(request, 'account_settings.html')