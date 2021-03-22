from rest_framework.serializers import ModelSerializer

from lectures.models import Lecture


class LectureSerializers(ModelSerializer):
    """Сериализация профиля"""

    class Meta:
        model = Lecture
        fields = ['id', 'subjects', 'author', 'title', 'text', 'created_date', 'published_date']




