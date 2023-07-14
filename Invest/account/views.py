from django.shortcuts import render

def chat(request):
    return render(request, 'chat.html')

def my_a(request):
    return render(request, 'my_a.html')

def favorite(request):
    return render(request, 'favorite.html')

def base_panel(request):
    return render(request, 'base_panel.html')