import tempfile
from PIL import Image
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT,  HTTP_200_OK , HTTP_202_ACCEPTED, HTTP_205_RESET_CONTENT , HTTP_401_UNAUTHORIZED
from django.contrib.auth import get_user_model
from status.models import Status
User = get_user_model()

class createUserApiTest(APITestCase):
    def setUp(self): # Default SetUp Function
        user = User.objects.create(username='msdevs', email='msdevs@hotmail.com')
        user.set_password('msdevs.11')
        user.save()
        new_status = Status.objects.create(user=user, content='New Testing Content')
        self.assertEqual(Status.objects.count() , 1)
                
    def test_User_creation(self): # Default Testing Function
        qs = User.objects.all()
        self.assertEqual(qs.count() , 1)


    def test_token_passing(self):
        auth_url = 'http://127.0.0.1:8000/api/auth/jwt/'
        
        auth_data = {
            'username':"msdevs",
            'password':'msdevs.11',
        }
        
        response = self.client.post(auth_url , auth_data , format='json')
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ token)
        
        
        
    def test_status_CRUD_without_image(self):
        self.test_token_passing()
        '''
        Create
        '''
        create_url = 'http://127.0.0.1:8000/api/status/list/'
        data = {
            'content':'Hello To Api Testing',
        }
        response = self.client.post(create_url , data , format='json') 
        print(response.data)      
        self.assertEqual(response.status_code , HTTP_201_CREATED)        
        self.assertEqual(Status.objects.count() , 2)
        '''
        Retrieve
        '''
        data_id = response.data.get('id')
        retreive_url ="http://127.0.0.1:8000/api/status/list/"+str(data_id)+'/'
        response = self.client.get(retreive_url , format='json')
        print(response.data) 
        self.assertEqual(response.status_code ,  HTTP_200_OK)
        '''
        Update
        '''        
        data_id = response.data.get('id')
        update_url ="http://127.0.0.1:8000/api/status/list/"+str(data_id)+'/'
        data ={
            'content':'Some New Content'
        }
        response = self.client.put(update_url , data, format='json')
        print(response.data) 
        self.assertEqual(response.status_code ,  HTTP_200_OK)
        '''
        Delete
        '''        
        data_id = response.data.get('id')
        delete_url ="http://127.0.0.1:8000/api/status/list/"+str(data_id)+'/'
        response = self.client.delete(delete_url, format='json')
        print(response.data)
        self.assertEqual(response.status_code ,  HTTP_204_NO_CONTENT)
        


    def test_status_CRUD_image(self):
        self.test_token_passing()
        '''
        Create
        '''
        create_url = 'http://127.0.0.1:8000/api/status/list/'
        image = Image.new('RGB' , (800 , 800), (0 , 125 , 175))
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpeg')
        image.save(temp_file, format='jpeg')
        with open(temp_file.name, 'r') as file_obj:
            data = {
                'content':'Hello To Api Testing',
                'image': file_obj
            }
            response = self.client.post(create_url , data , format='mutltipart') 
            print(response.data)      
            self.assertEqual(response.status_code , HTTP_201_CREATED)        
            self.assertEqual(Status.objects.count() , 2)
        '''
        Retrieve
        '''
        # data_id = response.data.get('id')
        # retreive_url ="http://127.0.0.1:8000/api/status/list/"+str(data_id)+'/'
        # response = self.client.get(retreive_url , format='json')
        # print(response.data) 
        # self.assertEqual(response.status_code ,  HTTP_200_OK)
        # '''
        # Update
        # '''        
        # data_id = response.data.get('id')
        # update_url ="http://127.0.0.1:8000/api/status/list/"+str(data_id)+'/'
        # data ={
        #     'content':'Some New Content'
        # }
        # response = self.client.put(update_url , data, format='json')
        # print(response.data) 
        # self.assertEqual(response.status_code ,  HTTP_200_OK)
        # '''
        # Delete
        # '''        
        # data_id = response.data.get('id')
        # delete_url ="http://127.0.0.1:8000/api/status/list/"+str(data_id)+'/'
        # response = self.client.delete(delete_url, format='json')
        # print(response.data)
        # self.assertEqual(response.status_code ,  HTTP_204_NO_CONTENT)





        
        
    # def test_status_creation_no_token(self):
    #     url = 'http://127.0.0.1:8000/api/status/list/'
    #     data = {
    #         'content':'Hello To Api Testing',
    #     }
    #     response = self.client.post(url , data , format='json') 
    #     print(response.data)      
    #     self.assertEqual(response.status_code , HTTP_401_UNAUTHORIZED)        
    #     self.assertEqual(Status.objects.count() , 2)
        
        
    # def test_register_user_api(self):
    #     url = 'http://127.0.0.1:8000/api/auth/register/'
        
    #     data = {
    #         'username':"MSdevs99",
    #         'email':'msdevs@gmail.com',
    #         'password':'MS123',
    #         'password2':'MS123',
    #     }
        
    #     response = self.client.post(url , data , format='json')
    #     print(response.status_code)
    #     #print(dir(response))
    #     print(response.data)
    #     token = response.data.get('access')
    #     print(token)
    #     self.assertEqual(response.status_code , HTTP_201_CREATED)
        
        
        
    # def test_user_get_token_api(self):
    #     url = 'http://127.0.0.1:8000/api/auth/jwt/'
        
    #     data = {
    #         'username':"msdevs",
    #         'password':'msdevs.11',
    #     }
        
    #     response = self.client.post(url , data , format='json')
    #     print(response.status_code)
    #     #print(dir(response))
    #     #print(response.data)
    #     token = response.data['access']
    #     print("Your Access Token :",token)
    #     self.assertEqual(response.status_code , HTTP_200_OK)
        
        
        
    # def test_user_token_info_api(self):
    #     url = 'http://127.0.0.1:8000/api/auth/jwt/'
        
    #     data = {
    #         'username':"msdevs",
    #         'password':'msdevs.11',
    #     }
        
    #     response = self.client.post(url , data , format='json')
    #     print(response.status_code)
    #     #print(dir(response))
    #     #print(response.data)
    #     token = response.data['access']
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ token)
    #     response2 = self.client.post(url , data , format='json')
    #     self.assertEqual(response2.status_code , HTTP_200_OK)