from rest_framework import serializers
from avto.models import Post, ContactInfo, SaveAndNote, RentToOwn
from option.serializers import PostOptionSerializer


class PostSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(source="district.title")
    subcategory = serializers.StringRelatedField(source="subcategory.title")
    options = PostOptionSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"


class RentToOwnSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentToOwn
        fields = "__all__"

class SaveAndNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveAndNote
        fields = "__all__"  


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__" 





