from django.db.models import Avg

from celery import shared_task




@shared_task
def set_avg_rating(item_id):
    '''
    подсчет среднего рейтинга
    :param item_id: принимает на входе id from models.Item
    :return:
    '''
    from .models import Item
    avg = Item.objects.filter(id=item_id)
    avgrate = avg.annotate(avgrate=Avg('reviews__rating')).values_list('avgrate', flat=True)[0]
    avg.update(avg_rating = round(avgrate,1))