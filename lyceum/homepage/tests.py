from django.test import Client, TestCase
from django.urls import reverse


class HomepageTests(TestCase):
    client = Client()

    def test_homepage(self):
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)

    def test_coffee_status_code(self):
        response = self.client.get(reverse("coffee"))
        self.assertEqual(response.status_code, 418)

    def test_coffee_body(self):
        response = self.client.get(reverse("coffee"))
        self.assertEqual(
            response.content.decode("utf-8"), "<body>Я чайник.</body>"
        )
