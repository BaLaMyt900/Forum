from django.contrib import admin
from django.urls import path, include
from main.views import index

urlpatterns = [
    path('', include('livechat.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('', index)
]
