from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard_main.html')

def enter(request):
    return render(request, 'dashboard_enter.html')

