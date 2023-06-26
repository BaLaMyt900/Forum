from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from announcement.models import Response


# TODO: таск рассылки при создании отзыва автору объявления

@shared_task
def new_responce_notification(pk):
    """ Задача по отправке сообщения автору объявления о новом отзыве на его объявлении """
    response = Response.objects.filter(pk=pk).values('text', 'announce__title', 'announce__author__email', 'author__username')
    context = {
        'user': response['author__username'],
        'text': response['text'],
        'title': response['announce__title']
    }
    message = render_to_string('announce/email/new_responce.html', context=context)

    mes = EmailMessage(
        f'Новый отзыв на Вашу статью!',
        message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=response['announce__author__email']
    )
    mes.content_type = 'html'
    mes.send()
