import django.test
import django.urls


class HomepageTests(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    def test_homepage(self):
        response = self.client.get(django.urls.reverse("homepage:homepage"))
        self.assertEqual(response.status_code, 200)

    def test_coffee_status_code(self):
        response = self.client.get(django.urls.reverse("homepage:coffee"))
        self.assertEqual(response.status_code, 418)

    def test_coffee_body(self):
        response = self.client.get(django.urls.reverse("homepage:coffee"))
        self.assertEqual(
            response.content.decode("utf-8"), "<body>Я чайник.</body>"
        )
