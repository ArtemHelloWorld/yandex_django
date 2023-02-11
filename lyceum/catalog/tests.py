from django.test import Client, TestCase


class CatalogTests(TestCase):
    def test_item_list(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_item_detail(self):
        response = Client().get("/", kwargs={"item_pk": 1})
        self.assertEqual(response.status_code, 200)
