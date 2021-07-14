from django.http import response
from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user_model, login
from .models import CustomUser


class Custom_Users_Tests(TestCase):

    def test_signup(self):
        response = self.client.post(reverse("signup")).status_code
        self.assertEqual(response, 200) 

    def test_login(self): 
        response = self.client.post(reverse('login')).status_code
        self.assertEqual(response , 200)
       