import json 
from django.db import models
from django.conf import settings
from django.core.serializers import serialize
from django.db.models.query import QuerySet

def upload_update_image(instance , filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

class UpdateQuerySet(models.QuerySet):
    # Method 1
    # def serialize(self):
    #     qs = self
    #     final_array = []
    #     for obj in qs:
    #         struct = json.loads(obj.serialize())
    #         final_array.append(struct)
    #     # this take a queryset and serialize this 
    #     return json.dumps(final_array)
    
    # Method 2
    def serialize(self):
        list_values = list(self.values('user', 'content', 'image', 'id'))
        print(list_values)
        # this take a queryset and serialize this 
        return json.dumps(list_values)
    
class UpdateManager(models.Manager):
    def get_queryset(self):
        #It takes the model that are used and database which is under usage 
        return UpdateQuerySet(self.model , using=self._db)


class update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = UpdateManager()
    
    def __str__(self):
        return self.content or ''
    
    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""
        data = {
            'id':self.id,
            'content':self.content,
            'user':self.user.id,
            'image':image,
        }
        
        # this take a queryset and serialize this 
        # json_data = serialize("json" , [self] , fields=('user' , 'content', 'image'))
        # struct = json.loads(json_data) # It changes data into python dictionary
        # print(struct)
        data = json.dumps(data)
        return data