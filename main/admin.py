from django.contrib import admin


from livechat.models import ChatMessage
from main.models import Category, Announcement, Response

# Register your models here.

admin.site.register(ChatMessage)
admin.site.register(Category)
admin.site.register(Announcement)
admin.site.register(Response)