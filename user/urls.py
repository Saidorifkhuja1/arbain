from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [

   path('register/', UserRegistrationAPIView.as_view()),
   path('verify-email/<uidb64>/<token>/',VerifyEmailAPIView.as_view(),name='verify-email'),
   path('login/', TokenObtainPairView.as_view()),
   path('profile_details/', RetrieveProfileView.as_view()),
   path('update_profile/<uuid:uid>/', UpdateProfileView.as_view()),
   path('reset_password/', PasswordResetView.as_view()),
   path('delete_profile/<uuid:uid>/', DeleteProfileAPIView.as_view()),

]

