from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.urls import reverse
from django.views.generic import View, DetailView
from django.views.generic import CreateView

from .models import Item, Reviews
from .forms import ItemForm, ReviewForm, ReviewImageForm
from account.models import Profile

from .tasks import set_avg_rating


def all_items(request):
    """
        Вьюшка для отображения всех объявлений
    """
    all_items = Item.objects.all()
    context = {
        'all_items': all_items
    }
    return render(request, 'item/item.html', context)


def iteminfo(request, item_id):
    """
        Вьюшка, которая показывает информацию об одном объявлении 
    """
    item = get_object_or_404(Item, id=item_id)
    item.count_view += 1
    creater_profile = Profile.objects.get(user=item.user)
    item.save()

    context = {
        'item': item,
        'creater_profile': creater_profile
    }
    return render(request, 'item/iteminfo.html', context)


def increment_count_phone_number_item(request):
    """
        Вьюха для обработки Ajax запросов на добавление +1 к счетчику
        вывода номера телефона на объявления
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        item = Item.objects.get(id=request.POST.get('item_id'))
        item.count_get_contacts += 1
        item.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


@login_required
def additem(request, errors=''):
    """
        Вьюшка для добавления нового объяления на сайт
    """
    if request.method == 'GET':
        return render(request, 'item/additem.html', context={'request': request, 'errors': errors})
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
            return redirect('iteminfo', item_id=item.id)
        return render(request, 'item/additem.html', context={'request': request, 'errors': form.errors})


@login_required
def edit_item(request, item_id):
    """
        Вьюшка для редактирования своих объявлений
    """
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'GET':
        form = ItemForm(instance=item)
        return render(request=request, template_name='item/edit_item.html', context={'form': form})

    form = ItemForm(data=request.POST, instance=item)

    if form.is_valid():
        if form.cleaned_data['user'].id == request.user.id:
            form.save()
            return redirect('iteminfo', item_id=item.id)
    return render(request=request, template_name='item/edit_item.html', context={'form': form, 'errors': form.errors})


@login_required
def delete_item(request, item_id):
    """
        Вьюшка для удаления объявления
    """
    Item.objects.get(id=item_id).delete()
    return redirect('my_items')


def about(request):
    return render(request, 'item/about.html')


def support(request):
    return render(request, 'item/support.html')


class CreateReview(LoginRequiredMixin, View):
    template_name = 'account/add_review.html'



    def get(self, request, *args, **kwargs):
        form1 = ReviewForm(prefix='form1')
        form2 = ReviewImageForm(prefix='form2')
        return render(request, context= ({'form1': form1, 'form2': form2}), template_name='account/add_review.html')

    def post(self, request, *args, **kwargs):
        review_form = ReviewForm(self.request.POST, prefix='form1')
        review_form.instance.user = request.user
        review_form.instance.item = Item.objects.get(pk  = self.kwargs['item_id'])
        image_form = ReviewImageForm(self.request.POST, self.request.FILES, prefix='form2')
        if review_form.is_valid():
            review_form.save()
            #set_avg_rating.delay(self.kwargs['item_id'])
        image_form.instance.review = review_form.instance
        if image_form.is_valid():
            image_form.save()
            return redirect('iteminfo', self.kwargs['item_id'])


@login_required
def my_reviews(request):
    '''
    показывает все отзывы залогиненного человека
    '''
    revs = Reviews.objects.all()
    return render(request, 'item/all_item_reviews.html', context={'revs':revs})

class ReviewDetail(LoginRequiredMixin, DetailView):
    template_name = 'item/review.html'
    model = Reviews
    context_object_name = 'review'

@login_required()
def review_delete(request, pk):
    get_object_or_404(Reviews, pk=pk).delete()
    return redirect('my_reviews')