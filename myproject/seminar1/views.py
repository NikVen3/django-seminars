import logging
import random
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
