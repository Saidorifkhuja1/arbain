from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from core.paginations import CustomPageNumberPagination
from .models import Hadis
from .serializers import HadisCreateSerializer, HadisListSerializer


# class HadisCreateView(generics.CreateAPIView):
#     queryset = Hadis.objects.all()
#     serializer_class = HadisCreateSerializer
#     permission_classes = [IsAdminUser]

#
# class HadisUpdateView(generics.UpdateAPIView):
#     queryset = Hadis.objects.all()
#     serializer_class = HadisCreateSerializer
#     lookup_field = 'uid'
#     permission_classes = [IsAdminUser]


class HadisDeleteView(generics.DestroyAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisCreateSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


class HadisSearchAPIView(generics.ListAPIView):
    serializer_class = HadisListSerializer
    pagination_class = CustomPageNumberPagination

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'search', openapi.IN_QUERY,
            description="Search term (applies to title, uzbek, arabic, description, data items, type, author)",
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
                Q(types__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(data_items__title__icontains=search_query) |
                Q(data_items__text__icontains=search_query)
            ).distinct()

        return queryset


class HadisListView(generics.ListAPIView):
    queryset = Hadis.objects.all().order_by('-date')
    serializer_class = HadisListSerializer
    pagination_class = CustomPageNumberPagination


class HadisRetrieveView(generics.RetrieveAPIView):
    queryset = Hadis.objects.all()
    serializer_class = HadisListSerializer
    lookup_field = 'uid'

