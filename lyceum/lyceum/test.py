import django.test
import django.urls

import parameterized


@parameterized.parameterized_class(
    ("url", "normal_body", "reversed_body"),
    [
        (
            django.urls.reverse("homepage"),
            "<body>Главная</body>",
            "<body>яанвалГ</body>",
        ),
        (
            django.urls.reverse("description"),
            "<body>О проекте</body>",
            "<body>О еткеорп</body>",
        ),
        (
            django.urls.reverse("item_list"),
            "<body>Список, элементов</body>",
            "<body>косипС, вотнемелэ</body>",
        ),
    ],
)
@django.test.override_settings(REVERSE_RU=True)
class ActiveReverseMiddlewareTestCase(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

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
        self.assertIn(
            self.reversed_body,
            responses_arr,
            f"Failed. reversed_body not in responses_arr. Url: {self.url}.",
        )


@parameterized.parameterized_class(
    ("url", "normal_body", "reversed_body"),
    [
        (
            django.urls.reverse("homepage"),
            "<body>Главная</body>",
            "<body>яанвалГ</body>",
        ),
        (
            django.urls.reverse("description"),
            "<body>О проекте</body>",
            "<body>О еткеорп</body>",
        ),
        (
            django.urls.reverse("item_list"),
            "<body>Список, элементов</body>",
            "<body>косипС, вотнемелэ</body>",
        ),
    ],
)
@django.test.override_settings(REVERSE_RU=False)
class InActiveReverseMiddlewareTestCase(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

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
            responses_arr,
            f"Failed. reversed_body in responses_arr. Url: {self.url}.",
        )
