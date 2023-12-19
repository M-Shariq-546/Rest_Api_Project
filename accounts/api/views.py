import json
from django.db.models import Q
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.contrib.auth import authenticate , get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializers, UserDetailPublicSerializer



User = get_user_model()

class AuthView(APIView):
    permission_classes = [AllowAny]
    def post(self, request , *args , **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response({"details":"You are already Authenticated. "}, status=201)
        data = request.data 
        username = data.get('username')
        password = data.get('password')
       # token = data.get('token')
       # user = authenticate(username=username , password=password)
        query_set = User.objects.filter(
            Q(username__iexact=username)|
            Q(password__iexact=password)
                ).distinct()
        if query_set.count() == 1:
            user_object = query_set.first()
            if user_object.check_password(password):
                user = user_object    
                print(user)
                return Response({'user':user})
        return Response({'Message':"Invalid Username or Password"}, status=399)
    
class UserDetailApiView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailPublicSerializer
    lookup_field = 'username'
    
    
class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers
    permission_classes = [AllowAny]
   
# class RegisterView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request , *args , **kwargs):
#         print(request.user)
#         if request.user.is_authenticated:
#             return Response({"details":"You are already REgistered and Authenticated. "}, status=201)
#         data = request.data 
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         password2 = data.get('password2')
#        # token = data.get('token')
#        # user = authenticate(username=username , password=password)
#         query_set = User.objects.filter(
#             Q(username__iexact=username)|
#             Q(password__iexact=password)
#                 ).distinct()
        
#         if password != password2:
            
#             return Response({'Alert':"Password Doesn't Match At All"}, status=500)
            
#         if query_set.exists():
#             # print(request.user.username)
#             return Response({'Message':"User Already Exists"}, status=201)
#         else:
#             user = User.objects.create(username=username , email=email)
#             user.set_password(password)
#             user.save()
#             new_user = UserRegistrationSerializers(user)
#             # user = json.dumps(user)
#             print(user)
#             return Response(json.dumps({'Message':"User is Successfully REgistered"}))
        
#         return Response({'Message':"Invalid Username or Password"}, status=399)