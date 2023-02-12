import os

from django.test import Client, TestCase
from django.urls import reverse
from parameterized import parameterized_class


@parameterized_class(("url", "normal_body", "reversed_body"), [
    (reverse("homepage"), "<body>Главная</body>", "<body>яанвалГ</body>"),
    (reverse("description"), "<body>О проекте</body>", "<body>О еткеорп</body>"),
    (reverse("item_list"), "<body>Список элементов</body>", "<body>косипС вотнемелэ</body>"),
])
class MyMiddlewareTestCase(TestCase):
    client = Client()

    def test_first_nine_requests(self):
        middleware_status = os.getenv("REVERSE_MIDDLEWARE", "False").lower()

        for i in range(10):
            response = self.client.get(self.url)

            if i == 9 and middleware_status in ("active", "true", "1"):
                expected_result = self.reversed_body
            else:
                expected_result = self.normal_body

            self.assertEqual(
                response.content.decode("utf-8"),
                expected_result,
                f"Failed with first 9 requests. Url: {self.url}. Step {i}",
            )
