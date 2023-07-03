from django.urls import path, include
from .views import JSONProfileGet


urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/<int:pk>', JSONProfileGet),
]
