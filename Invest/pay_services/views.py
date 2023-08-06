"""
    Представления для покупок на сайте
"""

from django.shortcuts import render


def pay_services(request):
    """
        Показывает все платные услуги
    """
    return render(request, 'pay_services.html')
