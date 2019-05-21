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
 





