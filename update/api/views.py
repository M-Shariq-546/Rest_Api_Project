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
        # Getting the Data based on assigned ID
        obj = self.get_object(id=pk)
        if obj is None:
            error_data = json.dumps({'message':"Update Not Found"})
            return self.render_to_response(error_data, status=404)
        
        previous_data = json.loads(obj.serialize())
        #changing the data into python dictionary
        passed_data = json.loads(request.body)
        # Now replace the old content with new updated content send via API Call
        for key , value in passed_data.items():
            previous_data['content'] = value
            
        form = UpdateModelForm(passed_data, instance=obj)
        if form.is_valid():
            data = form.save(commit=True)
            #Serializing the data into json
            json_data = json.dumps(previous_data) #data.serialize()
            return self.render_to_response(json_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        print("Changed Content is : ",passed_data['content'])
        json_data_message = json.dumps({'message':"Successfully Update Post updated"})
        return self.render_to_response(json_data_message) #json
    
    def delete(self , request, pk, *args , **kwargs): # It returns the delete Method
        obj = self.get_object(id=pk)
        if obj is None:
            error_data = json.dumps({'message':"Update Not Found on This Id"})
            return self.render_to_response(error_data, status=404)

        
        data = obj.delete()
        json_data = json.dumps({'message':'update is successfully deleted'})
        return self.render_to_response(json_data ,status=200) #json
        
    
# This is the class which handles all the CRUD Operation    
class UpdateModelListApiView(HTTPResponseMixin,CSRFExemptMixin , View):
    '''
    List --> Retrieve --> Detail View
    Create
    update
    delete
    '''
    is_json =True

    query_set = None
    
    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.query_set = qs
        return qs    
    
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
        if id is None:
            return None
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None
    
            
    def get(self , request, *args , **kwargs): # It returns the Get Method
        data = json.loads(request.body)
        passed_id = data.get('id')
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({'message':"Object Not Found"})
                return self.render_to_response(error_data, status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        else:
            qs = self.get_queryset()
            json_data = qs.serialize()
            return self.render_to_response(json_data)    
        


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
 
 
    def put(self , request,*args , **kwargs): # It returns the Put Method
        # Validating the json data format
        is_valid = is_json(request.body)
        if not is_valid:
            error_data = json.dumps({'message':"Not a json data please sent json data"})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({'id':"ID is required to update the data "})
            return self.render_to_response(error_data, status=400)
        # Getting the Data based on assigned ID
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({'message':"Object Not Found"})
            return self.render_to_response(error_data, status=404)
        previous_data = json.loads(obj.serialize())
        # Now replace the old content with new updated content send via API Call
        for key , value in passed_data.items():
            previous_data['content'] = value
            
        form = UpdateModelForm(passed_data, instance=obj)
        if form.is_valid():
            data = form.save(commit=True)
            #Serializing the data into json
            json_data = json.dumps(previous_data) #data.serialize()
            return self.render_to_response(json_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        print("Changed Content is : ",passed_data['content'])
        json_data_message = json.dumps({'message':"Successfully Update Post updated"})
        return self.render_to_response(json_data_message) #json
    
    def delete(self , request, *args , **kwargs): # It returns the delete Method 
        is_valid = is_json(request.body)
        if not is_valid:
            error_data = json.dumps({'message':"Not a json data please sent json data"})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({'id':"ID is required to delete the data "})
            return self.render_to_response(error_data, status=400)
        # Getting the Data based on assigned ID
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({'message':"Object Not Found"})
            return self.render_to_response(error_data, status=404)

        
        data = obj.delete()
        json_data = json.dumps({'message':'update is successfully deleted'})
        return self.render_to_response(json_data ,status=200) #json
 