from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserModelPublicSerializer
'''
serializers ->  can converted JSON
serializers -> can converted Validate Data
'''


class StatusSerializers(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserModelPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields = ['id','user' , 'content', 'image', 'uri']
        read_only_fields = ['user'] # On Get CAll user would be readonly and uses the
        # default logged in as current user
        
        
    def get_uri(self , obj):
        return "api/user/{id}".format(id=obj.id)
        
    # Serializers Validation same like forms Validation 
    # For more best Guests visit status.froms.py
    
    # Validation for Content Length
    def validate_content(self , value):
        if len(value) > 200:
            raise serializers.ValidationError("Content is Too Long . Reduce it to 200 Characters")
        return value
    
    # Validation of empty Content and Image Fields
    def validate(self , data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError("content and image are must fields . Please fill them")
        return data
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
    