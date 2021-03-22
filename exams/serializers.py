from rest_framework.serializers import ModelSerializer

from exams.models import Exam


class ExamSerializers(ModelSerializer):
    """Сериализация профиля"""

    class Meta:
        model = Exam
        fields = ['id', 'forgroup', 'subjects', 'author', 'theme', 'appraisal']





