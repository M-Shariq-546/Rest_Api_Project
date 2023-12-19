from django.urls import path, include
from .views import AuthView, RegisterApiView, UserDetailApiView

from rest_framework_simplejwt.views import TokenObtainPairView 

urlpatterns = [
    path('', AuthView.as_view()),
    path('user/<str:username>/', UserDetailApiView.as_view()),
    path('register/', RegisterApiView.as_view())
]

