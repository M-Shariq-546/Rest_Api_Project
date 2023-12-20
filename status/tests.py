from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Status
User = get_user_model()

class createUserTest(TestCase):
    def setUp(self): # Default SetUp Function
        user = User.objects.create(username='msdevs', email='msdevs@hotmail.com')
        user.set_password('msdevs.11')
        user.save()
        
    def test_Status_creation(self): # Default Testing Function
        user = User.objects.get(username='msdevs')
        new_status = Status.objects.create(user=user, content='Testing content or Testing app')
        self.assertEqual(new_status.id , 1)
        qs = Status.objects.all()
        self.assertEqual(qs.count() , 1)