from django.contrib.auth import get_user_model
from rest_framework import serializers
from status.api.serializer import StatusUserSerializers
#Getting the data from User Model 
User = get_user_model()
class UserDetailPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields =[
            'id',
            'username',
            'email',
            'uri',
            'status'
        ]

    def get_uri(self , obj):
        return "http://127.0.0.1:8000/api/users/{username}/".format(username=obj.username)

    def get_status(self , obj):
        data = {
            'uri':self.get_uri(obj),
            'last':self.get_last_status(obj),
            'recent_uploads':self.get_recent_status(obj)
        }
        return data


    def get_last_status(self , obj):
        qs = obj.status_set.all().order_by('-timestamp') # To limit the objects just add .[:Numbers_upto_reduce]
        #The Above This is equals to Status.objects.filter(user=obj)
        final_qs = qs.first()
        return StatusUserSerializers(final_qs , many=False).data

    def get_recent_status(self , obj):
        qs = obj.status_set.all().order_by('-timestamp') # To limit the objects just add .[:Numbers_upto_reduce]
        #The Above This is equals to Status.objects.filter(user=obj)
        return StatusUserSerializers(qs , many=True).data