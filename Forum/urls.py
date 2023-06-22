from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('livechat.urls')),
    path('', include('main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('profile.urls')),
]
