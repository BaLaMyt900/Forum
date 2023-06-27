from django.http import JsonResponse
from .models import Announcement, Response, Notification


def ajaxcreateresponse(request):
    """ Функция создания отзыва через ajax POST запрос """
    if request.method == 'POST':
        resp = Response.objects.create(text=request.POST.get('text'),
                                author=request.user,
                                announce=Announcement.objects.get(pk=request.POST.get('announce')))
        Notification.objects.create(object=resp)
    return JsonResponse(status=200, data={'object': 'OK'})
