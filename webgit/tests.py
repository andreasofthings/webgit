from django.test import TestCase
from django.test.client import Client

class TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def testPost(self):
        response = self.client.post("/")
