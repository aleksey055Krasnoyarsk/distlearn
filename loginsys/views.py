from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from loginsys.models import UserProfile, Groups, Subjects, Teachers, Students, Organizer
from loginsys.serializers import UserProfileSerializers, GroupsSerializers, SubjectsSerializers, TeachersSerializers, StudentsSerializers, OrganizerSerializers

# Create your views here.

class UserProfileView(ModelViewSet):
    """Профили"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers



class GroupView(ModelViewSet):
    """Группы"""
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializers


class SubjectsView(ModelViewSet):
    """Учебные дисциплины"""
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializers


class TeachersView(ModelViewSet):
    """Преподаватели"""
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializers

class StudentsView(ModelViewSet):
    """Студенты"""
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers

class OrganizerView(ModelViewSet):
    """Органайзеры"""
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializers



def loginsys(request):
    return render(request, 'loginsys/page.html')


def loginsys_app(request):
    return render(request, 'loginsys/main_app.html')