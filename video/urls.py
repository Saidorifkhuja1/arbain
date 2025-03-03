from django.urls import path
from .views import *

urlpatterns = [
    path('news_list/', VideosListView.as_view()),
    path('news_detail/<uuid:uid>/', VideosRetrieveView.as_view()),

]





