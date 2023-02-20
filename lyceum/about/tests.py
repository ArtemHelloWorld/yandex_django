import django.test
import django.urls


class AboutTests(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    def test_description(self):
        response = self.client.get(django.urls.reverse("description"))
        self.assertEqual(response.status_code, 200)
