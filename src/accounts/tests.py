from .forms import *
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserProfile

User = get_user_model()


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.username = "testuser"
        new_user = User.objects.create(username=self.username)

    def test_profile_created(self):
        username = self.username
        user_profile = UserProfile.objects.filter(user__username=self.username)
        self.assertTrue(user_profile.exists())
        self.assertTrue(user_profile.count()== 1)
 

class TestUser(TestCase):

    def test_login(self):
        response = self.client.post("/login", {"username": "lior", "password": "12345678a"})
        print(response.status_code)
        self.assertTrue(response.status_code == 301)
        self.assertTrue(self.client.get('/login').status_code == 301)             

    def test_logout(self):
        self.client = Client()
        self.client.login(username='lior', password='12345678a')
        self.assertTrue(self.client.get('/logout/').status_code== 302)






