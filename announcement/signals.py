from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Response
from .tasks import new_response_notification


@receiver(post_save, sender=Response)
def response_notyfication(sender, instance, created, **kwargs):
    """ Сигнал обрабатываемый при создании отзыва. Отправляет email автору объявления """
    if created:
        new_response_notification.apply_async([instance.pk])
