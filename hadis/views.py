from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from .models import *
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from drf_yasg import openapi

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
    serializer_class = HadisListSerializer
    pagination_class = CustomPagination

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'search', openapi.IN_QUERY,
            description="Search term (applies to title, uzbek, arabic, description, data)",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'limit', openapi.IN_QUERY,
            description="Number of results per page",
            type=openapi.TYPE_INTEGER
        ),
        openapi.Parameter(
            'offset', openapi.IN_QUERY,
            description="Offset (pagination start index)",
            type=openapi.TYPE_INTEGER
        ),
    ])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Hadis.objects.all()
        search_query = self.request.query_params.get('search', '').strip()

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(uzbek__icontains=search_query) |
                Q(arabic__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(data__icontains=search_query)
            )
        return queryset


class HadisListView(generics.ListAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisListSerializer
    pagination_class = CustomPagination

class HadisRetrieveView(generics.RetrieveAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisListSerializer
    lookup_field = 'uid'



