from django.urls import path, include
from .views import ProfileJSONView


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('profile/<int:pk>', ProfileJSONView.as_view()),
]
