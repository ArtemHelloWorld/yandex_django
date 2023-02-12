from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse


class CatalogTests(TestCase):
    client = Client()

    tests_positive_integers = {
        "0": 200,
        "1": 200,
        "12": 200,
        "125": 200,
        "10001": 200,
        "3432143": 200,
        "-1": 404,
        "-12": 404,
        "-154": 404,
        "-1343": 404,
        "-1456432": 404,
        "0.1": 404,
        "-0.1": 404,
        "1.1": 404,
        "-1.1": 404,
        "1.0001": 404,
        "-1.0001": 404,
        "2421341.454321": 404,
        "-2421341.454321": 404,
        "0,1": 404,
        "-0,1": 404,
        "1,1": 404,
        "-1,1": 404,
        "1,0001": 404,
        "-1,0001": 404,
        "2421341,454321": 404,
        "-2421341,454321": 404,
        "e": 404,
        "englishstring": 404,
        "с": 404,
        "строканарусском": 404,
        "*": 404,
        "*&873%": 404,
    }

    def test_item_list(self):
        response = self.client.get(reverse("item_list"))
        self.assertEqual(response.status_code, 200)

    def test_item_detail(self):
        for number, status in self.tests_positive_integers.items():
            try:
                url = reverse("item_detail", kwargs={"item_pk": number})
                response = self.client.get(url)
                self.assertEqual(
                    response.status_code, status, f"{number} failed"
                )
            except NoReverseMatch:
                self.assertEqual(404, status, f"{number} failed")

    def test_item_detail_re(self):
        for number, status in self.tests_positive_integers.items():
            try:
                url = reverse("item_detail_re", kwargs={"reint": number})
                response = Client().get(url)
                self.assertEqual(
                    response.status_code, status, f"{number} failed"
                )
            except NoReverseMatch:
                self.assertEqual(404, status, f"{number} failed")

    def test_custom_converter(self):
        for number, status in self.tests_positive_integers.items():
            try:
                url = reverse(
                    "custom_converter", kwargs={"custom_int": number}
                )
                response = self.client.get(url)
                self.assertEqual(
                    response.status_code, status, f"{number} failed"
                )
            except NoReverseMatch:
                self.assertEqual(404, status, f"{number} failed")
