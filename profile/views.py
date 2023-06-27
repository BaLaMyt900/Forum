from django.contrib.auth.models import User
from json_views.views import JSONDetailView
from announcement.models import Announcement, Response, Notification
from django.http import JsonResponse

class ProfileJSONView(JSONDetailView):
    """ JSON view профиля пользователя """
    model = User
    queryset = User.objects.all().values('pk', 'username', 'date_joined', 'email', 'first_name', 'last_name')

    def get_context_data(self, **kwargs):
        """ Сбор информации о пользователе, информация, объявления, отклики """
        context = super(ProfileJSONView, self).get_context_data(**kwargs)
        author = self.object['pk']
        context['announce'] = Announcement.objects.filter(author=author)
        context['response'] = Response.objects.filter(author=author)
        return context


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
