from rest_framework import serializers
from muhaddis.models import Muhaddis
from .models import Hadis, HadisData

from rest_framework import serializers
from .models import Hadis, HadisData

class HadisDataSerializer(serializers.ModelSerializer):
    """Serializer for HadisData, used inside HadisCreateSerializer"""
    class Meta:
        model = HadisData
        fields = ['uid','title', 'text']  # Only require fields the user should enter

class HadisCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Hadis with nested HadisData"""
    data = HadisDataSerializer()  # Allow entering HadisData details directly

    class Meta:
        model = Hadis
        fields = ['uid','number', 'title', 'uzbek', 'arabic', 'author', 'description', 'data']

    def create(self, validated_data):
        # Extract HadisData details from validated data
        hadis_data_info = validated_data.pop('data')

        # Create a new HadisData instance
        hadis_data_instance = HadisData.objects.create(**hadis_data_info)

        # Create and return Hadis instance with the newly created HadisData
        hadis_instance = Hadis.objects.create(data=hadis_data_instance, **validated_data)
        return hadis_instance

# Serializer for listing/retrieving operations
class HadisListSerializer(serializers.ModelSerializer):
    # Nesting the HadisData details
    data = HadisDataSerializer(read_only=True)
    # For the author, you might show a string representation or nest more details if needed.
    author = serializers.StringRelatedField()

    class Meta:
        model = Hadis
        fields = ['uid', 'title', 'uzbek', 'arabic', 'description', 'author', 'data', 'number']






