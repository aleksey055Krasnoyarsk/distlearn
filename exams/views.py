from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from exams.models import Exam
from exams.serializers import ExamSerializers

# Create your views here.


class ExamView(ModelViewSet):
    """Профили"""
    queryset = Exam.objects.all()
    serializer_class = ExamSerializers

def exams(request):
    return render(request, 'exams/page.html')