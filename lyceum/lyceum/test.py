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

        self.responses_arr = []
        for i in range(10):
            response = self.client.get(self.url)
            self.responses_arr.append(response.content.decode("utf-8"))

    def test_to_check_normal_response(self):
        self.assertIn(
            self.normal_body,
            self.responses_arr,
            f"Failed. Url: {self.url}.",
        )

    def test_to_check_reversed_response(self):
        self.assertIn(
            self.reversed_body,
            self.responses_arr,
            f"Failed. Url: {self.url}.",
        )


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
@override_settings(REVERSE_RU=False)
class InActiveReverseMiddlewareTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.responses_arr = []
        for i in range(10):
            response = self.client.get(self.url)
            self.responses_arr.append(response.content.decode("utf-8"))

    def test_to_check_normal_response(self):
        self.assertIn(
            self.normal_body,
            self.responses_arr,
            f"Failed. Url: {self.url}.",
        )

    def test_to_check_reversed_response(self):
        self.assertNotIn(
            self.reversed_body,
            self.responses_arr,
            f"Failed. Url: {self.url}.",
        )
