from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser

from hadis.views import CustomPagination
from .models import *
from .serializers import *

class VideosRetrieveView(generics.RetrieveAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    lookup_field = 'uid'


class VideosListView(generics.ListAPIView):
    queryset = Videos.objects.all().order_by('-uploaded_at')
    serializer_class = VideosSerializer
    pagination_class = CustomPagination


