from django.urls import path
from .views import UserChatSessionView, SendMessageView, SupportChatListView

urlpatterns = [
    path('session/', UserChatSessionView.as_view(), name='chat-session'),
    path('session/<int:session_id>/messages/', SendMessageView.as_view(), name='chat-send-message'),
    path('support/sessions/', SupportChatListView.as_view(), name='support-chat-list'),
]
