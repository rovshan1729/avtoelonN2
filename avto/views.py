from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, generics
from avto.models import Post
from avto.serializers import PostSerializer


# Create your views here.
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
