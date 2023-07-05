from django.urls import path
from .views import AnnouncementCreate, AnnounceView, AnnounceUpdate
from .ajax import ajaxcreateresponse, accept_response, remove_response

urlpatterns = [
    path('new/', AnnouncementCreate.as_view()),
    path('edit/<int:pk>', AnnounceUpdate.as_view()),
    path('<int:pk>/', AnnounceView.as_view()),
    path('ajax/new_response/', ajaxcreateresponse),
    path('ajax/accept_response/<int:pk>', accept_response),
    path('ajax/remove_response/<int:pk>', remove_response)
]