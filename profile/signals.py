from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(user_signed_up)
def allauth_user_signup(request, user, **kwargs):
    """ СигналЮ добавляющий новых пользователей в группу Users """
    user.groups.add(Group.objects.get(name='Users'))
    user.save()



