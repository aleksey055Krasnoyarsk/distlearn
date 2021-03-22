from rest_framework.serializers import ModelSerializer

from messenger.models import Message


class MessageSerializers(ModelSerializer):
    """Сериализация профиля"""

    class Meta:
        model = Message
        fields = ['id', 'to_user', 'from_user', 'text', 'date']
