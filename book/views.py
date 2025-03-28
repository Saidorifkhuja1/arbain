from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Book
from .serializers import BookSerializer, BookUpdateSerializer
from hadis.views import CustomPagination

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
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination


class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Retrieve books based on type query parameter.
        """
        book_type = self.kwargs.get('book_type')
        return Book.objects.filter(type=book_type)

