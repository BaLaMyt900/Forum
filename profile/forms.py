from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from allauth.socialaccount.forms import SignupForm as SocialSignupForm


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.groups.add(Group.objects.get(name='Users'))
        print('GROUP!')
        return user


class CustomSocialSignupForm(SocialSignupForm):
    def save(self, request):
        user = super(CustomSocialSignupForm, self).save(request)
        user.groups.add(Group.objects.get(name='Users'))
        print('GROUP!')
        return user