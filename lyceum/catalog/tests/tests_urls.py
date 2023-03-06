# import django.test
# import django.urls
# import parameterized
#
#
# @parameterized.parameterized_class(
#     ("number", "status"),
#     [
#         ("1", 200),
#         ("12", 200),
#         ("125", 200),
#         ("10001", 200),
#         ("3432143", 200),
#         ("-1", 404),
#         ("-12", 404),
#         ("-154", 404),
#         ("-1343", 404),
#         ("-1456432", 404),
#         ("0", 404),
#         ("0.1", 404),
#         ("-0.1", 404),
#         ("1.1", 404),
#         ("-1.1", 404),
#         ("1.0001", 404),
#         ("-1.0001", 404),
#         ("2421341.454321", 404),
#         ("-2421341.454321", 404),
#         ("0,1", 404),
#         ("-0,1", 404),
#         ("1,1", 404),
#         ("-1,1", 404),
#         ("1,0001", 404),
#         ("-1,0001", 404),
#         ("2421341,454321", 404),
#         ("-2421341,454321", 404),
#         ("e", 404),
#         ("englishstring", 404),
#         ("с", 404),
#         ("строканарусском", 404),
#         ("*", 404),
#         ("*&873%", 404),
#     ],
# )
# class CatalogDynamicTests(django.test.TestCase):
#     def setUp(self):
#         self.client = django.test.Client()
#
#     def test_item_detail(self):
#         url = f"/catalog/{self.number}/"
#         response = self.client.get(url)
#
#         self.assertEqual(
#             response.status_code, self.status, f"{self.number} failed"
#         )
#
#
# class CatalogStaticTests(django.test.TestCase):
#     def setUp(self):
#         self.client = django.test.Client()
#
#     def test_item_list(self):
#         response = self.client.get(django.urls.reverse("catalog:item_list"))
#         self.assertEqual(response.status_code, 200)
