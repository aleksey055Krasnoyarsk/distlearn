from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from homework.models import Task
from homework.serializers import TaskSerializers

# Create your views here.


class TaskView(ModelViewSet):
    """Профили"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

def homework(request):
    return render(request, 'homework/page.html')