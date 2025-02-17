from rest_framework import serializers
from .models import Writer



class WriterSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Writer
        fields = '__all__'

