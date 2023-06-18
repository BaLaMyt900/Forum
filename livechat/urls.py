from django.urls import path
from .views import get_latest_chat, chat_add_message, get_chat

urlpatterns = [
    path('api/get_latest_chat/<int:seconds_old>', get_latest_chat, name='get_latest_chat'),
    path('api/new_chat_message/', chat_add_message),
    path('api/get_chat/', get_chat),
]
