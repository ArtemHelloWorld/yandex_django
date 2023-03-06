import catalog.models
import django.forms.models
import django.test
import django.urls


class HomepageTests(django.test.TestCase):
    def setUp(self):
        self.client = django.test.Client()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.published_category = catalog.models.Category.objects.create(
            is_published=True,
            name="vfhgffgfgz",
            slug="published_category",
            weight=100,
        )
        cls.unpublished_category = catalog.models.Category.objects.create(
            is_published=False,
            name="Тестовая категория не опубликована",
            slug="unpublished_category",
            weight=100,
        )
        cls.image1 = catalog.models.ItemImageMain.objects.create(
            image_main="item/main/2023/02/26/shoes_w.jpg"
        )
        cls.image2 = catalog.models.ItemImageMain.objects.create(
            image_main="item/main/2023/02/26/sneakers_m.jpg"
        )
        cls.published_tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="Тестовый тег",
            slug="published_tag",
        )
        cls.unpublished_tag = catalog.models.Tag.objects.create(
            is_published=False,
            name="Тестовый тег не опубликован",
            slug="unpublished_tag",
        )

        cls.published_item = catalog.models.Item(
            is_published=True,
            name="Тестовый товар",
            category=cls.published_category,
            image=cls.image1,
            is_on_main=True,
        )
        cls.unpublished_item = catalog.models.Item(
            is_published=False,
            name="Тестовый товар не опубликован",
            category=cls.published_category,
            image=cls.image2,
            is_on_main=True,
        )

        cls.published_item.clean()
        cls.published_item.save()
        cls.unpublished_item.clean()
        cls.unpublished_item.save()

        cls.published_item.tags.add(cls.published_tag.pk)
        cls.published_item.tags.add(cls.unpublished_tag.pk)

    def test_homepage(self):
        response = self.client.get(django.urls.reverse("homepage:homepage"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_context(self):
        response = self.client.get(django.urls.reverse("homepage:homepage"))
        self.assertIn("items", response.context)

    def test_homepage_context_length(self):
        response = self.client.get(django.urls.reverse("homepage:homepage"))
        items = response.context["items"]
        self.assertEqual(len(items), 1)

    def test_homepage_context_values(self):
        response = self.client.get(django.urls.reverse("homepage:homepage"))
        items = response.context["items"]
        for i in items:
            self.assertEqual(
                [
                    "id",
                    "name",
                    "is_published",
                    "text",
                    "category",
                    "image",
                    "is_on_main",
                    "tags",
                ],
                list(django.forms.models.model_to_dict(i).keys()),
            )

    def test_coffee_status_code(self):
        response = self.client.get(django.urls.reverse("homepage:coffee"))
        self.assertEqual(response.status_code, 418)

    def test_coffee_body(self):
        response = self.client.get(django.urls.reverse("homepage:coffee"))
        self.assertEqual(
            response.content.decode("utf-8"), "<body>Я чайник.</body>"
        )
