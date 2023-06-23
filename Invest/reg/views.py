from django.shortcuts import render

def registration(request):
    return render(request, 'registration.html')

def authorization(request):
    return render(request, 'authorization.html')