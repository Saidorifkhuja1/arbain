from rest_framework import serializers
from .models import Muhaddis



class MuhaddisSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Muhaddis
        fields = '__all__'

