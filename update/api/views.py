import json
from .utils import is_json
from update.forms import UpdateModelForm
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

    def get_object(self , id=None):
        #Method #1
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        #return obj
        '''
        Below Code also handles the DoesNotExist Exception
        '''
        # Method 2
        qs = UpdateModel.objects.filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self , request, pk, *args , **kwargs): # It returns the Get Method
        #obj = UpdateModel.objects.get(id=pk)
        obj = self.get_object(id=pk)
        if obj is None:
            error_data = json.dumps({'message':"Update Not Found"})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)


    def post(self , request, *args , **kwargs): # It returns the Post Method
        json_data = json.dumps({'message':"Not Allowed ! please use /api/list/ endpoint to create a new update"})
        return self.render_to_response(json_data ,status=403) #json
    
    def put(self , request, pk,*args , **kwargs): # It returns the Put Method
        # Validating the json data format
        is_valid = is_json(request.body)
        if not is_valid:
            error_data = json.dumps({'message':"Not a json data please sent json data"})
            return self.render_to_response(error_data, status=400)
        
        obj = self.get_object(id=pk)
        if obj is None:
            error_data = json.dumps({'message':"Update Not Found"})
            return self.render_to_response(error_data, status=404)
        
        passed_data = json.loads(request.body)
        form = UpdateModelForm(passed_data, instance=obj)
        if form.is_valid():
            data = form.save(commit=True)
            json_data = data.serialize()
            return self.render_to_response(json_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        
        print("Changed Content is : ",passed_data['content'])
        json_data = json.dumps({'message':"Successfully Update Post updated"})
        return self.render_to_response(json_data) #json
    
    def delete(self , request, pk, *args , **kwargs): # It returns the delete Method
        obj = self.get_object(id=pk)
        if obj is None:
            error_data = json.dumps({'message':"Update Not Found"})
            return self.render_to_response(error_data, status=404)

        new_obj = json.loads(obj)
        is_valid = is_json(new_obj)
        if not is_valid:
            error_data = json.dumps({'message':"Not a json data please sent json data"})
            return self.render_to_response(error_data, status=400)
        new_data = json.loads(request.body)
        form = UpdateModelForm(new_data)
        if form.is_valid():
            data = form.delete()
            json_data = json.dumps({'message':'update is successfully deleted'})
            return self.render_to_response(json_data ,status=200) #json
        return self.render_to_response(new_data, status=400)
    
    
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
        #print(request.POST)
        is_valid = is_json(request.body)
        if not is_valid:
            error_data = json.dumps({'message':"Not a json data please sent json data"})
            return self.render_to_response(error_data, status=400)
        new_data = json.loads(request.body)
        form = UpdateModelForm(new_data)
        if form.is_valid():
            data = form.save(commit=True)
            json_data = data.serialize()
            return self.render_to_response(json_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {'message':"Not Allowed"}
        return self.render_to_response(data, status=400)
    
    def put(self , request, *args , **kwargs): # It returns the Put Method
        return #json
    
    def delete(self , request, *args , **kwargs): # It returns the delete Method
        data = json.dumps({'message':"You Cannot Delete A Complete List"})
        return self.render_to_response(data, status=403) #json