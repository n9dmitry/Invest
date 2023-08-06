from django.shortcuts import render

# Create your views here.


def chat(request):
    return render(request, 'messanger/chat.html')


def messenger(request):
    return render(request, 'messanger/messenger.html')
