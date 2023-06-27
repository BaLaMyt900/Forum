from django.urls import path, include
from .views import ProfileJSONView, ajaxgetnotifications


urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/<int:pk>', ProfileJSONView.as_view()),
    path('profile/ajax/update_notifications/<int:pk>', ajaxgetnotifications),
]
