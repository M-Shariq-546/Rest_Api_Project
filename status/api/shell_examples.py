#from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializer import StatusSerializers
from status.models import Status

obj = Status.objects.all()
serializer = StatusSerializers(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)

print(json_data)