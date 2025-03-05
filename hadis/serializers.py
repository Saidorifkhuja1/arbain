from rest_framework import serializers
from muhaddis.models import Muhaddis
from .models import Hadis, HadisData

class HadisDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HadisData
        fields = '__all__'

# Serializer for create/update operations
class HadisCreateSerializer(serializers.ModelSerializer):
    # Here, 'data' is expected as a primary key (id)
    class Meta:
        model = Hadis
        fields = '__all__'

# Serializer for listing/retrieving operations
class HadisListSerializer(serializers.ModelSerializer):
    # Nesting the HadisData details
    data = HadisDataSerializer(read_only=True)
    # For the author, you might show a string representation or nest more details if needed.
    author = serializers.StringRelatedField()

    class Meta:
        model = Hadis
        fields = ['uid', 'title', 'uzbek', 'arabic', 'description', 'author', 'data']






