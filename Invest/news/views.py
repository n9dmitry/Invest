from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm


def dashboard_news(request):
    return render(request, 'dashboard_news.html')


def news_list(request):
    # news = News.objects.all()
    return render(request, 'news_list.html'
                  # , {'news': news}
                  )

# def create_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('news_list')
#     else:
#         form = NewsForm()
#     return render(request, 'create_news.html', {'form': form})
#
# def edit_news(request, news_id):
#     news = News.objects.get(id=news_id)
#     if request.method == 'POST':
#         form = NewsForm(request.POST, instance=news)
#         if form.is_valid():
#             form.save()
#             return redirect('news_list')
#     else:
#         form = NewsForm(instance=news)
#     return render(request, 'edit_news.html', {'form': form, 'news': news})
#
# def delete_news(request, news_id):
#     news = News.objects.get(id=news_id)
#     if request.method == 'POST':
#         news.delete()
#         return redirect('news_list')
#     return render(request, 'delete_news.html', {'news': news})

# Конец новостей
