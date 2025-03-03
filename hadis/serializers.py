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


class HadisListSerializer(serializers.ModelSerializer):
    related_hadis = serializers.SerializerMethodField()
    class Meta:
        model = Hadis
        fields = ['uid', 'title', 'uzbek', 'arabic', 'description', 'author', 'related_hadis']
    def get_related_hadis(self, obj):

        related = Hadis.objects.filter(author=obj.author).exclude(uid=obj.uid)
        return [{'uid': hadis.uid, 'title': hadis.title, 'uzbek': hadis.uzbek} for hadis in related]