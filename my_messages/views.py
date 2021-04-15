from rest_framework import generics
from .serializers import MessageDetailSerializer, MessagesListSerializer
from .models import Message


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageDetailSerializer


class MessagesListView(generics.ListAPIView):
    serializer_class = MessagesListSerializer
    queryset = Message.objects.all()


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageDetailSerializer
    queryset = Message.objects.all()
