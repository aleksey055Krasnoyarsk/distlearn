from rest_framework.serializers import ModelSerializer

from homework.models import Task


class TaskSerializers(ModelSerializer):
    """Сериализация профиля"""

    class Meta:
        model = Task
        fields = ['id', 'forgroup', 'subjects', 'author', 'title', 'text', 'created_date', 'published_date']



