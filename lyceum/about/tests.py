import django.test
import django.urls


@django.test.override_settings(RATE_LIMIT_MIDDLEWARE=False)
class AboutTests(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    def test_description(self):
        response = self.client.get(django.urls.reverse("about:description"))
        self.assertEqual(response.status_code, 200)
