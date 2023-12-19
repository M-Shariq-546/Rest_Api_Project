from django.contrib.auth import get_user_model
from rest_framework import serializers
#Getting the data from User Model 
User = get_user_model()

class UserDetailPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields =[
            'id',
            'username',
            'email',
            'uri'
        ]

    def get_uri(self , obj):
        return "api/auth/user/{username}".format(username=obj.username)


class UserModelPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields =[
            'id',
            'username',
            'email',
            'uri'
        ]

    def get_uri(self , obj):
        return "api/user/{id}".format(id=obj.id)

class UserRegistrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input':'password'},write_only=True)
    message = serializers.CharField(style={'input':'text'},read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'message'
        ]

        extra_kwargs = {'password':{'write_only':True}}
    def get_message(self, obj):
        return "Thank You for Registering."
    
    
    def validate(self , data):
        pw = data.get('password')
        pw2 = data.get('password2')
        if pw != pw2:
            raise serializers.ValidationError("password Doesn't Match At All")
        return data
    
    def create(self , validate_data):
        print(validate_data)
        
        user = User.objects.create(
            username=validate_data.get('username'),
            email=validate_data.get('email')
        )
        
        user.set_password(validate_data.get('password'))
        user.save()
        return user