from django.test import Client, TestCase


class AboutTests(TestCase):
    def test_description(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
