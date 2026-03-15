from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer

class UserChatSessionView(generics.RetrieveAPIView):
    """View for normal user to get their active chat session or create one"""
    serializer_class = ChatSessionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        session, created = ChatSession.objects.get_or_create(
            user=self.request.user,
            is_open=True
        )
        return session

class SendMessageView(generics.CreateAPIView):
    """View to send a message in a specific session"""
    serializer_class = ChatMessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        session_id = self.kwargs['session_id']
        session = get_object_or_404(ChatSession, id=session_id)
        
        # Verify permissions: users can only send to their own session, support can send to any
        if not self.request.user.is_support and session.user != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You cannot send messages to this chat.")

        serializer.save(sender=self.request.user, session=session)

        # Mark messages to the recipient as unread (already default False), but maybe update session
        session.save() # triggers updated_at

class SupportChatListView(generics.ListAPIView):
    """View for support admins to list all open chat sessions"""
    serializer_class = ChatSessionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if not self.request.user.is_support:
            return ChatSession.objects.none()
        return ChatSession.objects.filter(is_open=True).order_by('-updated_at')
