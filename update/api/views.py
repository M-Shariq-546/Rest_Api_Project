import json
from django.views.generic import View
from django.http import HttpResponse
from update.models import update as UpdateModel
from .mixin import CSRFExemptMixin
from update.mixins import HTTPResponseMixin
class UpdateModelDetailApiView(HTTPResponseMixin , CSRFExemptMixin , View):
    '''
    Retrieve , update , delete --> object
    '''
    is_json = True
    def get(self , request, pk, *args , **kwargs): # It returns the Get Method
        obj = UpdateModel.objects.get(id=pk)
        json_data = obj.serialize()
        return self.render_to_response(json_data)


    def post(self , request, *args , **kwargs): # It returns the Post Method
        return self.render_to_response(json_data ,status=400) #json
    
    def put(self , request, *args , **kwargs): # It returns the Put Method
        return self.render_to_response(json_data, status=400) #json
    
    def delete(self , request, *args , **kwargs): # It returns the delete Method
        return self.render_to_response(json_data ,status=403) #json
    
    
class UpdateModelListApiView(HTTPResponseMixin,CSRFExemptMixin , View):
    '''
    List, Create
    '''
    is_json =True
    
    def get(self , request, *args , **kwargs): # It returns the Get Method
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)    
        return #json


    def post(self , request, *args , **kwargs): # It returns the Post Method
        data = json.dumps({'message':"New Data"})
        return self.render_to_response(data, status=400)
    
    def put(self , request, *args , **kwargs): # It returns the Put Method
        return #json
    
    def delete(self , request, *args , **kwargs): # It returns the delete Method
        data = json.dumps({'message':"You Cannot Delete A Complete List"})
        return self.render_to_response(data, status=403) #json