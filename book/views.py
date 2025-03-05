from aiohttp.web_response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser

from hadis.views import CustomPagination
from .models import Book
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from rest_framework import status


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAdminUser]




class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer  # Use the BookUpdateSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    def update(self, request, *args, **kwargs):
        # Custom logic for removing 'author' if it's not provided
        request_data = request.data.copy()
        if 'author' in request_data and not request_data['author']:
            del request_data['author']

        # Proceed with the update
        return super().update(request, *args, **kwargs)

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    # permission_classes = [IsAdminUser]
