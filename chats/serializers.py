from rest_framework import serializers

from .models import Message, Channel


class MessageSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = '__all__'

    def get_is_owner(self, obj):
        return obj.user == self.request.user 




class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = '__all__'
