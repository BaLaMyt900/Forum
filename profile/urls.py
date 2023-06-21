from django.urls import path
from .views import ProfileJSONView


urlpatterns = [
    path('profile/<int:pk>', ProfileJSONView.as_view()),
]
