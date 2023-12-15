from django.urls import path, include
from .views import UpdateModelDetailApiView, UpdateModelListApiView

urlpatterns = [
    path('detail/<int:pk>/', UpdateModelDetailApiView.as_view()),
    path('list/', UpdateModelListApiView.as_view()),
]
