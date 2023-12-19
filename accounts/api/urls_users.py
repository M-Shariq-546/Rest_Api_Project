from django.urls import path, include
from .views import UserDetailApiView

from rest_framework_simplejwt.views import TokenObtainPairView 

urlpatterns = [
    path('<int:pk>/', UserDetailApiView.as_view(), name='detail'),
]

