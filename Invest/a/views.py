from django.shortcuts import render, redirect

from django.shortcuts import render

def a(request):
    return render(request, 'a.html')

def adinfo(request):
    return render(request, 'adinfo.html')