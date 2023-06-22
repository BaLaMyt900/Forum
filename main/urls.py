from django.urls import path
from .views import IndexView, AnnounceView, NewAnnounceView

urlpatterns = [
    path('', IndexView.as_view()),
    path('announce/new/', NewAnnounceView.as_view()),
]