from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Item
from .forms import ItemForm
from account.models import Profile


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
            images = request.FILES.getlist('images')
            item: Item = form.save()
            for image in images:
                item.images.create(item_id=item.id, image=image)
            if not item.contacts:
                item.contacts = Profile.objects.get(
                    user=request.user).phone_number
                item.save()
            return redirect('iteminfo')
        return render(request, 'additem.html', context={'request': request, 'errors': form.errors})
