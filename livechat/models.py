from django.contrib.auth.models import User
from django.db import models


class ChatMessage(models.Model):
    """ Модель сообщения в чате """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=100, null=False)
    date = models.DateTimeField(auto_now_add=True)
