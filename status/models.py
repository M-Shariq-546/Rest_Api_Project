from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet

'''
JSON --> JavaScript Object Notation
'''



def upload_status_image(instance , filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass
    
class StatusManager(models.Manager):
    def get_queryset(self):
        #It takes the model that are used and database which is under usage 
        return StatusQuerySet(self.model , using=self._db)



class Status(models.Model): # same like instagram post , whatsapp status
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_status_image,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = StatusManager()
    
    def __str__(self):
        if self.content != '':
            return str(self.content)[:50] # This is 50 character content
        return 'No Content added'
    
    class Meta:
        verbose_name = 'Status Post'
        verbose_name_plural = 'Status Posts'
        
    @property
    def owner(self):
        return self.user