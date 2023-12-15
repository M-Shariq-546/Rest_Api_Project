from django.shortcuts import render
from .models import update
from .mixins import JsonResponceMixin
from django.http import JsonResponse , HttpResponse
from rest_framework import serializers
from django.core.serializers import serialize
import json
from django.views.generic import View

def update_model_detail_view(request):
    updates = update.objects.all()
    counts = updates.count()
    
    data = {
        'count': 1000,
        'updates':"Hello To the Future",
    }
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data , content_type='application/json')

class Update_data_View(View):
    def get(self, request, *args , **kwargs): # This function could be as post , delete
        # or patch as per requirements
        data = {
        'count': 1000,
        'updates':"Hello To the Future",
        }
    
        json_data = json.dumps(data)
    
        return HttpResponse(json_data , content_type='application/json')


#Updated for Query set
class updated_Single_Data_view(JsonResponceMixin , View):
    def get(self, request, *args , **kwargs):
        qs = update.objects.get(id=3)
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')
    
class updated_Data_view(JsonResponceMixin , View):
    def get(self, request, *args , **kwargs):
        qs = update.objects.all().serialize()
        json_data = qs
        #data = serialize("json" , qs )#, fields=('user' , 'content'))
        #data_fields = serialize("json" , qs, fields=('user' , 'content'))
        return HttpResponse(json_data , content_type='application/json')