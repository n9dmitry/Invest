from django.shortcuts import render, redirect
from .forms import AddsForm

from django.shortcuts import render

def ads(request):
    return render(request, 'ads.html')

# def create_ad(request):
#     if request.method == 'POST':
#         form = AddsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('ads_list')
#     else:
#         form = AddsForm()
#     return render(request, 'create_ad.html', {'form': form})