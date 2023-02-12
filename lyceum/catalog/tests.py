from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse

from parameterized import parameterized_class


@parameterized_class(
    ("number", "status"),
    [
        ("0", 200),
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
class CatalogDynamicEndpointsTests(TestCase):
    client = Client()

    def test_item_detail(self):
        try:
            url = reverse("item_detail", kwargs={"item_pk": self.number})
            response = self.client.get(url)
            status_code = response.status_code
        except NoReverseMatch:
            status_code = 404

        self.assertEqual(status_code, self.status, f"{self.number} failed")

    def test_item_detail_re(self):
        try:
            url = reverse("item_detail_re", kwargs={"reint": self.number})
            response = self.client.get(url)
            status_code = response.status_code
        except NoReverseMatch:
            status_code = 404

        self.assertEqual(status_code, self.status, f"{self.number} failed")

    def test_custom_converter(self):
        try:
            url = reverse(
                "custom_converter", kwargs={"custom_int": self.number}
            )
            response = self.client.get(url)
            status_code = response.status_code
        except NoReverseMatch:
            status_code = 404

        self.assertEqual(status_code, self.status, f"{self.number} failed")


class CatalogStaticEndpointsTests(TestCase):
    def test_item_list(self):
        response = self.client.get(reverse("item_list"))
        self.assertEqual(response.status_code, 200)
