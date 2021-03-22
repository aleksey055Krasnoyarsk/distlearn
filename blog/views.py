from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blog.models import Post
from blog.serializers import PostSerializers

# Create your views here.


class PostView(ModelViewSet):
    """Профили"""
    queryset = Post.objects.all()
    serializer_class = PostSerializers



def blog(request):
    return render(request, 'blog/page.html')