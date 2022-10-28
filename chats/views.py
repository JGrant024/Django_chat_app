from rest_framework import generics
from .models import Message, Channel
from .serializers import MessageSerializer, ChannelSerializer 
from .permissions import IsOwnerOrReadOnly


class MessageListAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(channel=self.kwargs['pk'])

    def preform_create(self, serializer):
        serializer.save(channel=self.kwargs['pk'], user=self.request.user)


class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class ChannelListAPIView(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
