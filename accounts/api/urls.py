from django.urls import path, include
from .views import AuthView, RegisterApiView

from rest_framework_simplejwt.views import TokenObtainPairView 


urlpatterns = [
    path('', AuthView.as_view()),
    path('register/', RegisterApiView.as_view())
]

