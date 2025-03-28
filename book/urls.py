from django.urls import path
from .views import *

urlpatterns = [
    path('books_list/', BookListView.as_view()),
    path('create_book/', BookCreateView.as_view()),
    path('book_detail/<uuid:uid>/', BookRetrieveView.as_view()),
    path('update_book/<uuid:uid>/', BookUpdateView.as_view()),
    path('delete_book/<uuid:uid>/', BookDeleteView.as_view()),

    path('books/<str:book_type>/', BookListView1.as_view()),
]

