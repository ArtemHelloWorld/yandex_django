from django.test import Client, TestCase, override_settings
from django.urls import reverse

from parameterized import parameterized_class


@parameterized_class(
    ("url", "reversed_body"),
    [
        (reverse("homepage"), "<body>яанвалГ</body>"),
        (
            reverse("description"),
            "<body>О еткеорп</body>",
        ),
        (
            reverse("item_list"),
            "<body>косипС, вотнемелэ</body>",
        ),
    ],
)
@override_settings(REVERSE_RU=True)
class ActiveReverseMiddlewareTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ten_requests(self):
        responses = []
        for i in range(10):
            response = self.client.get(self.url)
            responses.append(response.content.decode("utf-8"))

        self.assertIn(
            self.reversed_body,
            responses,
            f"Failed. Url: {self.url}.",
        )


@parameterized_class(
    ("url", "reversed_body"),
    [
        (reverse("homepage"), "<body>яанвалГ</body>"),
        (
            reverse("description"),
            "<body>О еткеорп</body>",
        ),
        (
            reverse("item_list"),
            "<body>косипС, вотнемелэ</body>",
        ),
    ],
)
@override_settings(REVERSE_RU=False)
class InActiveReverseMiddlewareTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ten_requests(self):
        responses = []
        for i in range(10):
            response = self.client.get(self.url)
            responses.append(response.content.decode("utf-8"))
        print(responses)

        self.assertNotIn(
            self.reversed_body,
            responses,
            f"Failed. Url: {self.url}.",
        )
