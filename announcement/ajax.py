from django.http import JsonResponse
from .models import Announcement, Response, Notification
from .tasks import new_response_notification


def ajaxcreateresponse(request):
    """ Функция создания отзыва через ajax POST запрос """
    if request.method == 'POST':
        resp = Response.objects.create(text=request.POST.get('text'),
                                author=request.user,
                                announce=Announcement.objects.get(pk=request.POST.get('announce')))
        Notification.objects.create(object=resp)
        new_response_notification.apply_async([resp.pk])
    return JsonResponse(status=200, data={'object': 'OK'})


def accept_response(request, pk):
    """ Функция публикация отзыва """
    if request.method == 'POST':
        object = Response.objects.get(pk=pk)
        object.is_accept = True
        object.save()
        Notification.objects.get(object=object).delete()
        return JsonResponse(status=200, data={})


def remove_response(request, pk):
    """ Функция удаления отзыва """
    Response.objects.get(pk=pk).delete()
    return JsonResponse(status=200, data={})
