from rest_framework import serializers

from .models import Creator


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        # fields = ('profile_image', 'name', 'bio', 'website', 'user')
        fields = '__all__'
        read_only_fields = ['user']
