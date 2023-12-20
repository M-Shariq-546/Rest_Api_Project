from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from django.contrib.auth import get_user_model
from status.models import Status
User = get_user_model()

class createUserApiTest(APITestCase):
    def setUp(self): # Default SetUp Function
        user = User.objects.create(username='msdevs', email='msdevs@hotmail.com')
        user.set_password('msdevs.11')
        user.save()
        
    def test_User_creation(self): # Default Testing Function
        qs = User.objects.filter(username='msdevs')
        self.assertEqual(qs.count() , 1)
        
    def test_register_user_api(self):
        url = 'http://127.0.0.1:8000/api/auth/register/'
        
        data = {
            'username':"MSdevs99",
            'email':'msdevs@gmail.com',
            'password':'MS123',
            'password2':'MS123',
        }
        
        response = self.client.post(url , data , format='json')
        print(response.status_code)
        #print(dir(response))
        print(response.data)
        token = response.data.get('access')
        print(token)
        self.assertEqual(response.status_code , HTTP_201_CREATED)
        
        
        
    def test_user_get_token_api(self):
        url = 'http://127.0.0.1:8000/api/auth/jwt/'
        
        data = {
            'username':"msdevs",
            'password':'msdevs.11',
        }
        
        response = self.client.post(url , data , format='json')
        print(response.status_code)
        #print(dir(response))
        #print(response.data)
        token = response.data['access']
        print("Your Access Token :",token)
        self.assertEqual(response.status_code , HTTP_200_OK)
        
        
        
    def test_user_token_info_api(self):
        url = 'http://127.0.0.1:8000/api/auth/jwt/'
        
        data = {
            'username':"msdevs",
            'password':'msdevs.11',
        }
        
        response = self.client.post(url , data , format='json')
        print(response.status_code)
        #print(dir(response))
        #print(response.data)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ token)
        response2 = self.client.post(url , data , format='json')
        self.assertEqual(response2.status_code , HTTP_200_OK)