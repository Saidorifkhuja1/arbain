from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100





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
    pagination_class = CustomPagination

class HadisRetrieveView(generics.RetrieveAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisListSerializer
    lookup_field = 'uid'



