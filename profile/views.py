from django.contrib.auth.models import User
from django.shortcuts import redirect

from announcement.models import Announcement, Response, Notification
from django.http import JsonResponse
from Forum.tasks import newsletter


def JSONProfileGet(request, pk):
    """ JSON запрос информации профиля пользователя """
    user = User.objects.get(pk=pk)
    if user:
        data = {'object': {'username': user.username, 'email': user.email,
                           'first_name': user.first_name, 'last_name': user.last_name}}
        if Announcement.objects.filter(author=user).exists():
            data['announce'] = list(Announcement.objects.filter(author=user).values('pk', 'title'))
        if Response.objects.filter(author=user).exists():
            data['response'] = list(Response.objects.filter(author=user).values('is_accept', 'announce__title',
                                                                                'announce_id'))
        if Notification.objects.filter(object__announce__author=user).exists():
            announce_list = Announcement.objects.filter(author=user)
            notifications = {}
            for announce in announce_list:
                notifications[announce.pk] = Notification.objects.filter(object__announce=announce).count()
            notifications['sum'] = sum(notifications.values())
            data['notifications'] = notifications
        else:
            data['notifications'] = {}
        return JsonResponse(status=200, data=data)


def testcelery(request):
    newsletter.apply_async([])
    return redirect('/')
