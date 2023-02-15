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

    def test_to_check_responses(self):
        responses_arr = []
        for i in range(10):
            response = self.client.get(self.url)
            responses_arr.append(response.content.decode("utf-8"))

        self.assertIn(
            self.normal_body,
            self.responses_arr,
            f"Failed. normal_body not in responses_arr. Url: {self.url}.",
        )
        self.assertIn(
            self.reversed_body,
            self.responses_arr,
            f"Failed. reversed_body not in responses_arr. Url: {self.url}.",
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

    def test_to_check_responses(self):
        responses_arr = []
        for i in range(10):
            response = self.client.get(self.url)
            responses_arr.append(response.content.decode("utf-8"))

        self.assertIn(
            self.normal_body,
            responses_arr,
            f"Failed. normal_body not in responses_arr. Url: {self.url}.",
        )
        self.assertNotIn(
            self.reversed_body,
            self.responses_arr,
            f"Failed. reversed_body in responses_arr. Url: {self.url}.",
        )
