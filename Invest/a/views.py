from django.shortcuts import render, redirect

from django.shortcuts import render

def item(request):
    return render(request, 'item.html')

def iteminfo(request):
    return render(request, 'iteminfo.html')

def additem(request):
    return render(request, 'additem.html')