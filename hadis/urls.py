from django.urls import path
from .views import *

urlpatterns = [
    path('hadis/', HadisListView.as_view()),
    path('create_hadis/', HadisCreateView.as_view()),
    path('detail_hadis/<uuid:uid>/', HadisRetrieveView.as_view()),
    path('update_hadis/<uuid:uid>/', HadisUpdateView.as_view()),
    path('delete_hadis/<uuid:uid>/', HadisDeleteView.as_view()),
]
