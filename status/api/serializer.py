from rest_framework import serializers
from status.models import Status

'''
serializers ->  can converted JSON
serializers -> can converted Validate Data
'''


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','user' , 'content', 'image']
        
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
    
    
    
    
    