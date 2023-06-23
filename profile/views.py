from django.contrib.auth.models import User, Group
from json_views.views import JSONDetailView
from announcement.models import Announcement, Response
from allauth.account.forms import SignupForm


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


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        user.groups.add(Group.objects.get(name='Users'))
        return user

