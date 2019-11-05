from rest_framework import serializers

from .models import Image, Comment, Like


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('file', 'location', 'caption', 'creator')
        read_only_fields = ['creator','id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('message', 'creator')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
