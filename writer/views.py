from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from hadis.views import CustomPagination
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser

class WriterCreateView(generics.CreateAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class WriterRetrieveView(generics.RetrieveAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAdminUser]


class WriterUpdateView(generics.UpdateAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class WriterDeleteView(generics.DestroyAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


class WriterListView(generics.ListAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    pagination_class = CustomPagination
    # permission_classes = [IsAdminUser]
