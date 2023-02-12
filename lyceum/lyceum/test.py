import os

from django.urls import reverse
from django.test import Client, TestCase


class MyMiddlewareTestCase(TestCase):
    client = Client()
    tests = {
        reverse("homepage"): ["<body>Главная</body>", "<body>яанвалГ</body>"],
        reverse("description"): ["<body>О проекте</body>", "<body>О еткеорп</body>"],
        reverse("item_list"): ["<body>Список элементов</body>", "<body>косипС вотнемелэ</body>"],
    }

    def test_my_middleware(self):

        for url, content in self.tests.items():

            # first 9 requests
            for i in range(9):
                response = self.client.get(url)
                self.assertEqual(
                    response.content.decode("utf-8"),
                    content[0],
                    f"Failed with first 9 requests. Url: {url}"
                )

            # last 10th request
            response = self.client.get(url)
            if os.getenv("REVERSE_MIDDLEWARE", "False").lower() in ('active', 'true', '1'):
                self.assertHTMLEqual(
                    response.content.decode("utf-8"),
                    content[1],
                    f"Did not changed content. Url: {url}"
                )
            else:
                self.assertHTMLEqual(
                    response.content.decode("utf-8"),
                    content[0],
                    f"Changed content, but REVERSE_MIDDLEWARE=False. Url: {url}"
                )
