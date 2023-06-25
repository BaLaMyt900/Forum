from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now as time


class Category(models.Model):
    """ Категория объявления форума """
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    """ Модель объявления форума """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    text = models.CharField(max_length=555, null=False)
    date = models.DateTimeField(default=time)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title if len(self.title) < 25 else self.title[:22] + '...'

    class Meta:
        ordering = ('date', )


class Response(models.Model):
    """ Отклик на объявлление форума """
    is_accept = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    announce = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    text = models.TextField(max_length=300, null=False)
    date = models.DateTimeField(default=time)

    class Meta:
        ordering = ('-date', )

