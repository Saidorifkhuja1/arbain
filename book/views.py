from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser

from core.paginations import CustomPageNumberPagination
from .models import Book
from .serializers import *


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'uid'

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all().order_by('-uid')
    serializer_class = BookSerializer
    pagination_class = CustomPageNumberPagination


class BookListView1(generics.ListAPIView):
    serializer_class = BookSerializer1

    def get_queryset(self):
        """
        Retrieve books based on type query parameter.
        """
        book_type = self.kwargs.get('book_type')
        return Book.objects.filter(type=book_type)

