from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class createUserTest(TestCase):
    def setUp(self): # Default SetUp Function
        user = User.objects.create(username='msdevs', email='msdevs@hotmail.com')
        user.set_password('msdevs.11')
        user.save()
        
    def test_User_creation(self): # Default Testing Function
        qs = User.objects.filter(username='msdevs')
        self.assertEqual(qs.count() , 1)