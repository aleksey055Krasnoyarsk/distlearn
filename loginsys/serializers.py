from rest_framework.serializers import ModelSerializer

from loginsys.models import UserProfile, Groups, Subjects, Teachers, Students, Organizer


class UserProfileSerializers(ModelSerializer):
    """Сериализация профиля"""

    class Meta:
        model = UserProfile
        fields = ['id', 'status', 'login', 'status_ed', 'name', 'adress', 'number', 'email', 'license', 'certificate', 'boss', 'url_for_mess']




class GroupsSerializers(ModelSerializer):
    """Сериализация групп"""

    class Meta:
        model = Groups
        fields = ['id', 'group']



class SubjectsSerializers(ModelSerializer):
    """Сериализация учебных дисциплин"""

    class Meta:
        model = Subjects
        fields = ['id', 'subject']



class TeachersSerializers(ModelSerializer):
    """Сериализация преподавателей"""

    class Meta:
        model = Teachers
        fields = ['id', 'status', 'login', 'password', 'fio', 'position', 'number', 'email', 'education', 'degree', 'date_b', 'date_j', 'url_for_mess']


class StudentsSerializers(ModelSerializer):
    """Сериализация учеников"""

    class Meta:
        model = Students
        fields = ['id', 'login', 'fio', 'date', 'parents', 'number', 'group', 'url_for_mess']


class OrganizerSerializers(ModelSerializer):
    """Сериализация органайзера"""

    class Meta:
        model = Organizer
        fields = ['id', 'task', 'day', 'month', 'year']



