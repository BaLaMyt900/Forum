from django.contrib import admin
from django.urls import path, include
from main.views import index, AnnouncementCreate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('livechat.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('profile.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', index),
    path('announce/new/', AnnouncementCreate.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
