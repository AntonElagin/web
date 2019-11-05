from rest_framework import serializers
from .models import Comment

from .models import Image, Comment, Like




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'creator']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('file', 'location', 'caption', 'creator', 'comments')
        read_only_fields = ['creator','id']




class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['id', 'date']
