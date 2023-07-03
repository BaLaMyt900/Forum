import datetime
from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from announcement.models import Announcement


@shared_task
def newsletter():
    """ Задача отправки последних новостей всем пользователям """
    users = User.objects.all().values('username', 'email')
    week = int(datetime.datetime.today().strftime('%V')) - 1
    announce_list = Announcement.objects.filter(date__week=week).values('pk', 'title')
    for user in users:
        mes = EmailMessage(
            'Новостная рассылка с нашего форума!',
            render_to_string('announce/email/newsletter.html', context={'user': user['username'], 'list': announce_list}),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user['email']]
        )
        mes.content_subtype = 'html'
        mes.send()


