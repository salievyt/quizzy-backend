from rest_framework import serializers
from .models import ChatSession, ChatMessage
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatMessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)
    is_support = serializers.BooleanField(source='sender.is_support', read_only=True)

    class Meta:
        model = ChatMessage
        fields = ('id', 'sender', 'sender_name', 'is_support', 'content', 'timestamp', 'is_read')
        read_only_fields = ('id', 'sender', 'timestamp', 'is_read')

class ChatSessionSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = ('id', 'user', 'user_name', 'created_at', 'updated_at', 'is_open', 'messages')
        read_only_fields = ('id', 'user', 'created_at', 'updated_at', 'messages')
