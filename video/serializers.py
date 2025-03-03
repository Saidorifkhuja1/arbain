from rest_framework import serializers
from .models import Videos

class VideosSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    video = serializers.ImageField(required=True)
    class Meta:
        model = Videos
        fields = ['uid', 'title', 'body', 'video', 'image']


