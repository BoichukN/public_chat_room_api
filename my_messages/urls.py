from django.urls import path
from .views import *

urlpatterns = [
    path('message/create/', MessageCreateView.as_view()),
    path('single/<int:pk>/', MessageDetailView.as_view()),
    path('list/', MessagesListView.as_view()),
]
