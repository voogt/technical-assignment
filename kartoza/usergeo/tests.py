import unittest

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import User_Info
from django.test import Client
from django.utils import timezone


class TestUserGeo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(first_name='Big', last_name='Bob')

    def test_index(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        client = Client()
        response = client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        client = Client()
        response = client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_view_profile(self):
        client = Client()
        response = client.get("/profile/")
        self.assertEqual(response.status_code, 302)




