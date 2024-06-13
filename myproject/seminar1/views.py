import logging
import random
from django.http import HttpResponse

from datetime import date, timedelta

from django.db.models import Sum, F

from myapp.models import Client, Order, Product, OrderProducts
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a', format='%(levelname)s %(message)s')


def seminar1(request):
    logger.info(f'{request} request received')
    return HttpResponse("Seminar1 page")


def heads_tails(request):
    logger.info(f'{request} request received!')
    return HttpResponse(random.choice(['Орел', 'Решка']))


def dice(request):
    logger.info(f'{request} request received!')
    return HttpResponse(random.randint(1, 6))


def rand(request):
    logger.info(f'{request} request received')
    return HttpResponse(random.randint(1, 100))


def home(request):
    html = '<!DOCTYPE html>' \
           '<html lang="en">' \
           ' <head><meta charset="UTF-8"> ' \
           ' <title>Title</title>' \
           '</head> ' \
           '<body> ' \
           '<h1> Homepage </h1>' \
           '</body>' \
           ' </html>'
    logger.info(f'{request} request received')
    return HttpResponse(html)


def about(request):
    html = '<!DOCTYPE html>' \
           '<html lang="en">' \
           ' <head><meta charset="UTF-8"> ' \
           ' <title>Title</title>' \
           '</head> ' \
           '<body> ' \
           '<h1> About me </h1>' \
           '</body>' \
           ' </html>'
    logger.info(f'{request} request received')
    return HttpResponse(html)

def index(request):
    """Главная страница."""
    return render(request, 'index.html')


def about(request):
    """Страница About."""
    return render(request, 'about.html')


def clients_list(request):
    """Список клиентов."""
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'clients_list.html', context)


def client_orders(request, client_id):
    """Отображение заказов пользователя.

    :client_id: код клиента, по которому проводится выборка
    """
    client = get_object_or_404(Client, pk=client_id)
    # orders = Order.objects.prefetch_related('products').select_related('order_prods').filter(client_id=client_id)

    order_prods = OrderProducts.objects.select_related('product').select_related('order').filter(
        order__client_id=client_id).order_by('-order_id')

    order_prods = order_prods.annotate(prod_cost=F('product__price') * F('product_count'))

    context = {
        'client_name': client.client_name,
        'orders': order_prods,
    }

    return render(request, 'client_orders.html', context)


def client_prods(request, client_id, days_history):
    """
    Список товаров заказанных клиентом за определенное кол-во дней.

    :client_id: клиент по которому проводится выборка
    :days_history: кол-во дней, за которые проводится просмотр истории
    """
    client = get_object_or_404(Client, pk=client_id)
    date_start = date.today() - timedelta(days=days_history)

    prod_info = OrderProducts.objects.select_related('product').select_related('odrders').filter(
        order__order_date__gte=date_start, order__client_id=client_id)
    prod_info = prod_info.values('product__prod_name', 'product__price').annotate(count_prod=Sum('product_count'))
    prod_info = prod_info.annotate(cost=F('product__price') * F('count_prod'))

    context = {
        'client_name': client.client_name,
        'period': period(days_history),
        'products': prod_info
    }

    return render(request, 'client_products.html', context)


def period(days: int) -> str:
    """Период отчетности."""
    match days:
        case 7:
            return 'за последнюю неделю'
        case 30:
            return 'за последний месяц'
        case 365:
            return 'за последний год'
    return 'за произвольный период'
