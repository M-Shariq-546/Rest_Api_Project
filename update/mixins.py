from django.http import JsonResponse , HttpResponse


class HTTPResponseMixin(object):
    is_json = False 
    
    def render_to_respone(self, data , status=200):
        content_type = 'text/html'
        if self.is_json:
            content_type = 'application/json'
            
        return HttpResponse(data , content_type=content_type, status = status)



class JsonResponceMixin(object):
    def render_to_json_responce(self, context, **kwargs):
        return JsonResponse(self.get_data(context), **kwargs)
    
    # Take model or instance of that model and convert it to somehow to json
    def get_data(self , context):
        return context