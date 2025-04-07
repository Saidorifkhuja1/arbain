from rest_framework import serializers
from .models import Hadis, Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['uid', 'title', 'text']


class HadisCreateSerializer(serializers.ModelSerializer):
    data_items = DataSerializer(many=True, required=False)

    class Meta:
        model = Hadis
        fields = ['uid', 'number', 'title', 'uzbek', 'arabic', 'types', 'author', 'description', 'data_items']

    def create(self, validated_data):
        data_items_data = validated_data.pop('data_items', [])
        hadis = Hadis.objects.create(**validated_data)

        for data_item in data_items_data:
            Data.objects.create(hadis=hadis, **data_item)

        return hadis

    def update(self, instance, validated_data):
        data_items_data = validated_data.pop('data_items', [])

        # Update Hadis fields
        instance.number = validated_data.get('number', instance.number)
        instance.title = validated_data.get('title', instance.title)
        instance.uzbek = validated_data.get('uzbek', instance.uzbek)
        instance.arabic = validated_data.get('arabic', instance.arabic)
        instance.types = validated_data.get('types', instance.types)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Handle data items if provided
        if data_items_data:
            # Option 1: Replace all existing data items
            # instance.data_items.all().delete()

            # Option 2: Keep existing data items and add new ones
            for data_item in data_items_data:
                Data.objects.create(hadis=instance, **data_item)

        return instance


class HadisListSerializer(serializers.ModelSerializer):
    data_items = DataSerializer(many=True, read_only=True)

    class Meta:
        model = Hadis
        fields = ['uid', 'title', 'uzbek', 'arabic', 'types', 'author', 'description', 'data_items', 'number']

