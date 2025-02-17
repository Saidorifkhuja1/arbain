from rest_framework import serializers

from muhaddis.models import Muhaddis
from .models import Hadis

class HadisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hadis
        fields = '__all__'

class HadisSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Hadis
        exclude = ['author']

    # author = serializers.PrimaryKeyRelatedField(queryset=Muhaddis.objects.all(), required=False, write_only=True)
    #
    # class Meta:
    #     model = Hadis
    #     fields = '__all__'

