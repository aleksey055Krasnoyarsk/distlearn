from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from lectures.models import Lecture
from lectures.serializers import LectureSerializers

# Create your views here.


class LectureView(ModelViewSet):
    """Профили"""
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializers

def lectures(request):
    return render(request, 'lectures/page.html')