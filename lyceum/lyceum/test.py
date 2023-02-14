from django.test import Client, TestCase, override_settings
from django.urls import reverse

from parameterized import parameterized_class


@parameterized_class(
    ("url", "normal_body", "reversed_body"),
    [
        (reverse("homepage"), "<body>Главная</body>", "<body>яанвалГ</body>"),
        (
            reverse("description"),
            "<body>О проекте</body>",
            "<body>О еткеорп</body>",
        ),
        (
            reverse("item_list"),
            "<body>Список, элементов</body>",
            "<body>косипС, вотнемелэ</body>",
        ),
    ],
)
@override_settings(REVERSE_RU=True)
class ActiveReverseMiddlewareTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ten_requests(self):
        for i in range(10):
            response = self.client.get(self.url)

            if i == 9:
                expected_result = self.reversed_body
            else:
                expected_result = self.normal_body

            self.assertEqual(
                response.content.decode("utf-8"),
                expected_result,
                f"Failed on step {i}. Url: {self.url}.",
            )


@parameterized_class(
    ("url", "normal_body"),
    [
        (reverse("homepage"), "<body>Главная</body>"),
        (
            reverse("description"),
            "<body>О проекте</body>",
        ),
        (
            reverse("item_list"),
            "<body>Список, элементов</body>",
        ),
    ],
)
@override_settings(REVERSE_RU=False)
class InActiveReverseMiddlewareTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ten_requests(self):
        for i in range(10):
            response = self.client.get(self.url)
            self.assertEqual(
                response.content.decode("utf-8"),
                self.normal_body,
                f"Failed on step {i}. Url: {self.url}.",
            )
