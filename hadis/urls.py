from django.urls import path
from .views import *

urlpatterns = [
    path('hadis/', HadisListView.as_view()),
    path('create_hadis/', HadisCreateView.as_view()),
    path('detail_hadis/<uuid:uid>/', HadisRetrieveView.as_view()),
    path('update_hadis/<uuid:uid>/', HadisUpdateView.as_view()),
    path('delete_hadis/<uuid:uid>/', HadisDeleteView.as_view()),
    path('hadis/search/', HadisSearchAPIView.as_view()),

    path('hadisdata/create/', HadisDataCreateView.as_view()),
    path('hadisdata/update/<uuid:uid>/', HadisDataUpdateView.as_view()),
    path('hadisdata/delete/<uuid:uid>/', HadisDataDeleteView.as_view()),
    path('hadisdata/list/', HadisDataListView.as_view()),
    path('hadisdata/<uuid:uid>/', HadisDataRetrieveView.as_view()),
]
