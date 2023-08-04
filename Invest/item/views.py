from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ItemForm


def all_items(request):
    """
        Вьюшка для отображения всех объявлений
    """
    return render(request, 'item.html')


def iteminfo(request):
    return render(request, 'iteminfo.html')


@login_required
def additem(request, errors=''):
    """
        Вьюшка для добавления нового объяления на сайт
    """
    if request.method == 'GET':
        return render(request, 'additem.html', context={'request': request, 'errors': errors})
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iteminfo')
        return redirect('addinfo', errors=form.errors)
