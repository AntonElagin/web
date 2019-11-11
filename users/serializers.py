from rest_framework import serializers

from .models import Creator


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        # fields = ('profile_image', 'name', 'bio', 'website', 'user')
        fields = '__all__'
        exclude = 'password'
        read_only_fields = ['username', 'email']


# Реально не используется
class CreatorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            "password": {"write_only": True},
        }
