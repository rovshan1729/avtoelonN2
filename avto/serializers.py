from rest_framework import serializers
from avto.models import Post
from option.serializers import PostOptionSerializer


class PostSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(source="district.title")
    subcategory = serializers.StringRelatedField(source="subcategory.title")
    options = PostOptionSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
