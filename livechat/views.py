import django.utils.timezone
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import ChatMessage


def get_latest_chat(request, seconds_old):
    """ Получение последних сообщений """
    chat_since = django.utils.timezone.now() - django.utils.timezone.timedelta(seconds=seconds_old)
    chat = list(ChatMessage.objects.filter(date__gte=chat_since).values('author__username', 'text'))
    return JsonResponse(chat, safe=False)


def get_chat(request):
    """ Запрос последних восьми сообщений при переходе на страницу """
    chat = list(ChatMessage.objects.all().order_by('-date').values('author__username', 'text')[:8])
    chat.reverse()
    return JsonResponse(chat, safe=False)


def chat_add_message(request):
    """ Функция добавления нового сообщения в чат """
    author = request.user if not request.user.is_anonymous else User.objects.get(username='Аноним')
    text = request.POST.get('text')
    new_message = ChatMessage.objects.create(author=author, text=text)
    data = {'author': new_message.author.username, 'text': new_message.text}
    return JsonResponse(status=200, data=data)
