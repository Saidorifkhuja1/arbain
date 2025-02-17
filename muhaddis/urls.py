from django.urls import path
from .views import *



urlpatterns = [
    path('muhaddis_list/', MuhaddisListView.as_view()),
    path('create_muhaddis/', MuhaddisCreateView.as_view()),
    path('muhaddis_detail/<uuid:uid>/', MuhaddisRetrieveView.as_view()),
    path('update_muhaddis/<uuid:uid>/', MuhaddisUpdateView.as_view()),
    path('delete_muhaddis/<uuid:uid>/', MuhaddisDeleteView.as_view()),

]
