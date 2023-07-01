from django.contrib.auth.models import User
from django.core import serializers

from announcement.models import Announcement, Response, Notification
from django.http import JsonResponse


def JSONProfileGet(request, pk):
    """ JSON запрос информации пользователя профиля пользователя """
    user = User.objects.get(pk=pk)
    if user:
        data = {'object': {'username': user.username, 'email': user.email,
                           'first_name': user.first_name, 'last_name': user.last_name}}
        if Announcement.objects.filter(author=user).exists():
            data['announce'] = list(Announcement.objects.filter(author=user).values('pk', 'title'))
        if Response.objects.filter(author=user).exists():
            data['response'] = list(Response.objects.filter(author=user).values('is_accept', 'announce__title',
                                                                                'announce_id'))
        return JsonResponse(status=200, data=data)


def ajaxgetnotifications(request, pk):  # TODO: Сделать выборку колличества уведомлений по pk пользователя
    """ AJAX запрос уведомлений """
    author = User.objects.get(pk=pk)
    if Notification.objects.filter(object__announce__author=author).exists():
        announce_list = Announcement.objects.filter(author=author)
        data = {}
        for announce in announce_list:
            data[announce.pk] = Notification.objects.filter(object__response__announce=announce).count()
        print(data)
        return JsonResponse(status=200, data={'notifications': data})
    else:
        return JsonResponse(status=201, data={})


