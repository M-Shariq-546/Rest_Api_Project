from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView
from restapi.restconf.pagination import RestApiAppPagination
from status.api.views import StatusApiView
from rest_framework.pagination import PageNumberPagination
from .serializers import UserDetailPublicSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from accounts.api.permissions import IsOwnerOrReadOnly
from status.api.serializer import StatusUserSerializers
from status.models import Status
User = get_user_model()

class UserDetailApiView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailPublicSerializer
    lookup_field = 'username'
    
    
class UserStatusApiListView(StatusApiView): # This is bringing the functionality of StatusApiView
    # serializer_class = StatusUserSerializers
    # pagination_class = RestApiAppPagination
    # search_fields = ('user__username', 'content')
    #The above lines would be used in case of inheritance from ListAPIView
    def get_queryset(self , *args,**kwargs):
        username = self.kwargs.get('username', None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)
    
    def post(self , request , *args , **kwargs):
        return Response({"Alert":"Not Allowed Here"}, status=399)