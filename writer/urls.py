from django.urls import path
from .views import *



urlpatterns = [
    path('writers_list/', WriterListView.as_view()),
    path('create_writer/', WriterCreateView.as_view()),
    path('writer_detail/<uuid:uid>/', WriterRetrieveView.as_view()),
    path('update_writer/<uuid:uid>/', WriterUpdateView.as_view()),
    path('delete_writer/<uuid:uid>/', WriterDeleteView.as_view()),

]
