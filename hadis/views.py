from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from .models import Hadis
from .serializers import *


class HadisCreateView(generics.CreateAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisSerializer
    permission_classes = [IsAdminUser]


# class HadisRetrieveView(generics.RetrieveAPIView):
#     queryset = Hadis.objects.all()
#     serializer_class = HadisSerializer
#     lookup_field = 'uid'
#     # permission_classes = [IsAdminUser]

class HadisUpdateView(generics.UpdateAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisSerializer1
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


class HadisDeleteView(generics.DestroyAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


# class HadisListView(generics.ListAPIView):
#     queryset = Hadis.objects.all()
#     serializer_class = HadisSerializer
#     # permission_classes = [IsAdminUser]


class HadisSearchAPIView(generics.ListAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'uzbek']




class HadisListView(generics.ListAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisListSerializer

class HadisRetrieveView(generics.RetrieveAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisListSerializer
    lookup_field = 'uid'