from rest_framework import serializers
from .models import Hadis

class HadisCreateSerializer(serializers.ModelSerializer):

    data = serializers.ListField(child=serializers.JSONField(), required=False)

    class Meta:
        model = Hadis
        fields = ['uid', 'number', 'title', 'uzbek', 'arabic', 'description', 'data']

    def create(self, validated_data):

        return Hadis.objects.create(**validated_data)


class HadisListSerializer(serializers.ModelSerializer):

    data = serializers.ListField(child=serializers.JSONField(), read_only=True)


    class Meta:
        model = Hadis
        fields = ['uid', 'title', 'uzbek', 'arabic', 'description', 'data', 'number']