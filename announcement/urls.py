from django.urls import path
from .views import AnnouncementCreate, AnnounceView
from .ajax import ajaxcreateresponse, accept_response, remove_response

urlpatterns = [
    path('new/', AnnouncementCreate.as_view()),
    path('<int:pk>/', AnnounceView.as_view()),
    path('responce/new/', ajaxcreateresponse),
    path('ajax/accept_response/<int:pk>', accept_response),
    path('ajax/remove_response/<int:pk>', remove_response)
]