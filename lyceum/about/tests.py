from django.test import Client, TestCase
from django.urls import reverse


class AboutTests(TestCase):
    client = Client()

    def test_description(self):
        response = self.client.get(reverse('description'))
        self.assertEqual(response.status_code, 200)
