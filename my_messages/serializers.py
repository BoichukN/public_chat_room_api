from rest_framework import serializers
from .models import Message


class MessageDetailSerializer(serializers.ModelSerializer):
    email = serializers.RegexField(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', min_length=5)
    text = serializers.RegexField(r'\S+', max_length=100, min_length=1)

    class Meta:
        model = Message
        fields = '__all__'


class MessagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('email', 'text',)
