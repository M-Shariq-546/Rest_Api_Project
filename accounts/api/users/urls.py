from django.urls import path
from accounts.api.users.views import UserDetailApiView, UserStatusApiListView

urlpatterns = [
    path('<str:username>/', UserDetailApiView.as_view()),
    path('<str:username>/status/', UserStatusApiListView.as_view()),
]