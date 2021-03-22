from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from messenger.models import Message
from messenger.serializers import MessageSerializers

# Create your views here.


class MessageView(ModelViewSet):
    """Профили"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializers

def messenger(request):
    return render(request, 'messenger/page.html')