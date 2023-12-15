from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args , **kwargs): #this method is for all type of methods
        return super().dispatch(*args, **kwargs)