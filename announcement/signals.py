from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Response

@receiver(post_save, signal=Response)
def resposnse_notyfi(sender, instance, created, **kwargs):
    """ Сигнал обрабатываемый при создании отзыва. Отправляет email автору объявления """
    if created:
        print(f'CREATED {sender}')
        print(f'INSTANCE {instance}')