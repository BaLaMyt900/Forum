from django.shortcuts import render
from .models import Announcement, Response
from itertools import chain
from django.http import JsonResponse


def LastActivityAjax(request):
    """ Функция показа последней активности на сайте """
    annonce = Announcement.objects.all()[:4]
    response = Response.objects.all()[:4]
    activity = list(chain(annonce, response))
    if request.POST.get('list') == activity:
        return JsonResponse(status=201, data=None)
    else:
        return JsonResponse(status=200, data={'list': activity})




def index(request):
    return render(request, 'index.html')

