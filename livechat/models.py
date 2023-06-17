from django.db import models
from django.contrib.auth.models import User


class ChatMessage(models.Model):
    """ Модель собщения в чате """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=150, null=False)