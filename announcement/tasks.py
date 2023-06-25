from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import Announcement


# TODO: таск рассылки при создании отзыва автору объявления