from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)

from rest_framework.mixins import ( ListModelMixin,
                                    CreateModelMixin, 
                                    RetrieveModelMixin,
                                    UpdateModelMixin,
                                    DestroyModelMixin,)

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from status.models import Status
from .serializer import StatusSerializers
import json
from .utils import is_json
#from django.views.generic import View

class StatusDetailApiView(
                        UpdateModelMixin,
                        DestroyModelMixin,
                        RetrieveAPIView   ):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    
    # def get(self, request , *args, **kwargs):
    #     return self.get(request , *args, **kwargs)    
  
    def put(self, request , *args, **kwargs):
        return self.update(request , *args, **kwargs)
    
    def patch(self, request , *args, **kwargs):
        return self.update(request , *args, **kwargs)

    def delete(self ,request , *args, **kwargs):
        return self.destroy(request , *args, **kwargs)
            
class StatusApiView(CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializers
    passed_id = None
    # The below Code is used to having search functionality like
    # http://127.0.0.1:8000/api/get_status/list/
    
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)        
        return qs
    
    # def get_object(self):
    #     request = self.request
    #     passed_id = request.GET.get('id', None) or self.passed_id
    #     queryset = self.get_queryset()
    #     object = None
    #     if passed_id is not None:
    #         object = get_object_or_404(queryset , id=passed_id)
    #         self.check_object_permissions(request , object)
    #     return object
    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None 
    
    # def get(self , request , *args, **kwargs):
    #     request = self.request
    #     passed_id = request.GET.get('id', None)
    #     url_passed_id = request.GET.get('id', None) or self.passed_id
    #     json_data = {}
    #     if is_json(request.body):
    #         json_data = json.loads(request.body)
    #     new_passed_id = json_data.get('id', None)
    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     if passed_id is not None:
    #         return self.retrieve(request, *args , **kwargs)
    #     return super().get(request, *args , **kwargs)
    
    
     # This could handle the post method for adding data to api for us
    def post(self , request , *args , **kwargs):
        return self.create(request, *args , **kwargs)
    
    # We will come back to it when needed 
    # def perform_create(self , serializer):
    #     serializer.save(user=self.request.user)
    
    
    
# class StatusRetrieveApiView(RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializers
    
# The Above function works exact same as below given function    
    
# class StatusRetrieveApiView(DestroyModelMixin,UpdateModelMixin , RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializers
#     #lookup_field = 'id' # If we want to use id as parameter in our urls 
    
#     def put(self , request , *args , **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self , request , *args , **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self , request , *args , **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
    # By using kwargs we can also pass the pk / id in url
    # The below Function can be used but here i'm gonna use the built-in
    # def get_object(self , *args , **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('pk')
    #     return Status.objects.get(id=kw_id)
    
#class StatusUpdateApiView(UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializers
#     #lookup_field = 'id' # If we want to use id as parameter in our urls   
    
    
# class StatusDeleteApiView(DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializers
#     #lookup_field = 'id' # If we want to use id as parameter in our urls 