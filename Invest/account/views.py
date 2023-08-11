"""
    Представления для приложения Account
"""

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from item.models import Item
from .models import Profile
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_str 
from .token import account_activation_token
from django.core.mail import EmailMessage 
from .forms import ItemForm
from account.models import Profile
from .forms import RegistrationForm
from .forms import SignupForm

def authorization(request):
    return render(request, 'account/authorization.html')

def my_items(request):
    """
        Представление показывает все Items на странице
    """
    user_items = Item.objects.filter(user=request.user)
    context = {
        'user_items': user_items
    }
    return render(request, 'account/my_items.html', context)

def favorites(request):
    """
        Представление показывает избранные Item пользователя
    """
    profile = Profile.objects.get(user=request.user)
    context = {
        'favorites_items': profile.favorites.all()
    }
    return render(request, 'account/favorites.html', context)

def add_to_favorite(request):
    """
        Вьюха для обработки Ajax запросов на добавление в избранное
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        item = Item.objects.get(id=request.POST.get('item_id'))
        item.count_add_favorite.add(request.user)
        item.save()
        profile = Profile.objects.get(user=request.user)

        profile.favorites.add(item)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

def account_panel(request):
    """
        Панель действий связанных с аккаунтом
    """
    return render(request, 'account/account_tempalte_panel.html')

def account_settings(request):
    """
        Показывает настройки аккаунта
    """
    return render(request, 'account/account_settings.html')

def signup(request):
    """
        Вьюшка для регистрации через почту
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.username = '_'.join([request.POST['name'], str(user.pk)])
            user.save()

            Profile(    
                user=user,
                phone_number=request.POST['phone_number'],
                avatar = request.FILES['avatar'],
                interest=request.POST['interest']
                ).save()

            current_site = get_current_site(request)
            mail_subject = 'Ссылка для активации отправлена ​​на ваш адрес электронной почты'
            message = render_to_string('account/acc_activate_email.html',
                {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                }
            )
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject,
                message,
                to=[to_email]
            )
            email.send()
            return render(request, 'account/verify.html', {'message':'Вам на почту была отправленна ссылка для активации аккаунта! Письмо может быть в спаме.'})
        else:
            return render(request, 'account/registration.html', {'form':form, 'errors':form.errors})

    if request.method == 'GET':
        form = SignupForm()
    return render(request, 'account/registration.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        Profile.objects.get(user=user).save()
        return render(request, 'account/verify.html', {'message':'Спасибо за регистрацию, ваш аккаунт активен!'})
    else:
        return render(request, 'account/verify.html', {'message':'Извините, но ссылка более не действительна!'})
