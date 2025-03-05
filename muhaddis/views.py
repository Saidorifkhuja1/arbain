from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from hadis.views import CustomPagination
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser

class MuhaddisCreateView(generics.CreateAPIView):
    queryset = Muhaddis.objects.all()
    serializer_class = MuhaddisSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class MuhaddisRetrieveView(generics.RetrieveAPIView):
    queryset = Muhaddis.objects.all()
    serializer_class = MuhaddisSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAdminUser]


class MuhaddisUpdateView(generics.UpdateAPIView):
    queryset = Muhaddis.objects.all()
    serializer_class = MuhaddisSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]


class MuhaddisDeleteView(generics.DestroyAPIView):
    queryset = Muhaddis.objects.all()
    serializer_class = MuhaddisSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]


class MuhaddisListView(generics.ListAPIView):
    queryset = Muhaddis.objects.all()
    serializer_class = MuhaddisSerializer
    pagination_class = CustomPagination
    # permission_classes = [IsAdminUser]
