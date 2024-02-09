from rest_framework import generics
from avto.models import Post, ContactInfo, SaveAndNote, RentToOwn
from avto.serializers import PostSerializer, ContactInfoSerializer, SaveAndNoteSerializer, RentToOwnSerializer


# Create your views here.
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ContactInfoAPIView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class SaveAndNoteAPIView(generics.ListAPIView):
    queryset = SaveAndNote.objects.all()
    serializer_class = SaveAndNoteSerializer

class RentToOwnAPIView(generics.ListAPIView):
    queryset = RentToOwn.objects.all()
    serializer_class = RentToOwnSerializer