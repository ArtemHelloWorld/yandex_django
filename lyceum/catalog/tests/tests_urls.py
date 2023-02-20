import django.test
import django.urls

import parameterized


@parameterized.parameterized_class(
    ("number", "status"),
    [
        ("1", 200),
        ("12", 200),
        ("125", 200),
        ("10001", 200),
        ("3432143", 200),
        ("-1", 404),
        ("-12", 404),
        ("-154", 404),
        ("-1343", 404),
        ("-1456432", 404),
        ("0.1", 404),
        ("-0.1", 404),
        ("1.1", 404),
        ("-1.1", 404),
        ("1.0001", 404),
        ("-1.0001", 404),
        ("2421341.454321", 404),
        ("-2421341.454321", 404),
        ("0,1", 404),
        ("-0,1", 404),
        ("1,1", 404),
        ("-1,1", 404),
        ("1,0001", 404),
        ("-1,0001", 404),
        ("2421341,454321", 404),
        ("-2421341,454321", 404),
        ("e", 404),
        ("englishstring", 404),
        ("с", 404),
        ("строканарусском", 404),
        ("*", 404),
        ("*&873%", 404),
    ],
)
class CatalogDynamicTests(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    def test_item_detail(self):
        url = f"/catalog/{self.number}/"
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, self.status, f"{self.number} failed"
        )

    def test_item_detail_re(self):
        url = f"/catalog/re/{self.number}/"
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, self.status, f"{self.number} failed"
        )

    def test_custom_converter(self):
        url = f"/catalog/converter/{self.number}/"
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, self.status, f"{self.number} failed"
        )


class CatalogDynamicUniqueTests(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    @parameterized.parameterized.expand([("0", 200)])
    def test_item_detail_unique(self, number, status):
        url = f"/catalog/{number}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status, f"{number} failed")

    @parameterized.parameterized.expand([("0", 404)])
    def test_item_detail_re_unique(self, number, status):
        url = f"/catalog/re/{number}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status, f"{number} failed")

    @parameterized.parameterized.expand([("0", 404)])
    def test_custom_converter_unique(self, number, status):
        url = f"/catalog/converter/{number}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status, f"{number} failed")


class CatalogStaticTests(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    def test_item_list(self):
        response = self.client.get(django.urls.reverse("item_list"))
        self.assertEqual(response.status_code, 200)
