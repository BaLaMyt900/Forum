from django.contrib import admin
from django.urls import path, include
from main.views import index

urlpatterns = [
    path('', include('livechat.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('profile.urls')),
    path('', index)
]
