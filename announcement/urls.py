from django.urls import path
from .views import AnnouncementCreate, AnnounceView
from .ajax import ajaxcreateresponse

urlpatterns = [
    path('new/', AnnouncementCreate.as_view()),
    path('<int:pk>/', AnnounceView.as_view()),
    path('responce/new/', ajaxcreateresponse),
]