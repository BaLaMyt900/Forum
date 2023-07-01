from django.urls import path, include
from .views import JSONProfileGet, ajaxgetnotifications


urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/<int:pk>', JSONProfileGet),
    path('profile/ajax/update_notifications/<int:pk>', ajaxgetnotifications),
]
