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
        return JsonResponse(status=200, data=data)



def ajaxgetnotifications(request, pk):  # TODO: Сделать выборку колличества уведомлений по pk пользователя
    """ AJAX запрос уведомлений """
    if request.method == 'GET':
        announce_list = Announcement.objects.filter(author_id=pk)
        notifications = {}
        for announce in announce_list:
            count = Notification.objects.filter(object_id=announce.pk).count()
            if count:
                notifications[f'{announce.pk}'] = count
        return JsonResponse(status=200, data={'notifications': notifications})
    # if request.method == 'GET':
    #     announce_notifications = Notification.objects.filter(object__announce_id=pk).count()
    #     return JsonResponse(status=200, data={'count': announce_notifications})
