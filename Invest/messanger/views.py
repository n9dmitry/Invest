from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def chat(request):
    return render(request, 'messanger/chat.html')


def messenger(request):
    return render(request, 'messanger/messenger.html')
