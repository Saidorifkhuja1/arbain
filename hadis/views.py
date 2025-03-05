from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *

class HadisCreateView(generics.CreateAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisCreateSerializer
    permission_classes = [IsAdminUser]


class HadisUpdateView(generics.UpdateAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisCreateSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]

class HadisDeleteView(generics.DestroyAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisCreateSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]

class HadisSearchAPIView(generics.ListAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'uzbek']

class HadisListView(generics.ListAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisListSerializer

class HadisRetrieveView(generics.RetrieveAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisListSerializer
    lookup_field = 'uid'




class HadisDataCreateView(generics.CreateAPIView):
    queryset = HadisData.objects.all()
    serializer_class = HadisDataSerializer
    permission_classes = [IsAdminUser]

class HadisDataUpdateView(generics.UpdateAPIView):
    queryset = HadisData.objects.all()
    serializer_class = HadisDataSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]

class HadisDataDeleteView(generics.DestroyAPIView):
    queryset = HadisData.objects.all()
    serializer_class = HadisDataSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]

class HadisDataListView(generics.ListAPIView):
    queryset = HadisData.objects.all()
    serializer_class = HadisDataSerializer

class HadisDataRetrieveView(generics.RetrieveAPIView):
    queryset = HadisData.objects.all()
    serializer_class = HadisDataSerializer
    lookup_field = 'uid'