from rest_framework.serializers import ModelSerializer

from blog.models import Post


class PostSerializers(ModelSerializer):
    """Сериализация профиля"""

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'created_date', 'published_date']


