from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from parameterized import parameterized, parameterized_class

from .models import Category, Item, Tag


@parameterized_class(
    ("number", "status"),
    [
        ("1", 200),
        ("12", 200),
        ("125", 200),
        ("10001", 200),
        ("3432143", 200),
        ("-1", 404),
        ("-12", 404),
        ("-154", 404),
        ("-1343", 404),
        ("-1456432", 404),
        ("0.1", 404),
        ("-0.1", 404),
        ("1.1", 404),
        ("-1.1", 404),
        ("1.0001", 404),
        ("-1.0001", 404),
        ("2421341.454321", 404),
        ("-2421341.454321", 404),
        ("0,1", 404),
        ("-0,1", 404),
        ("1,1", 404),
        ("-1,1", 404),
        ("1,0001", 404),
        ("-1,0001", 404),
        ("2421341,454321", 404),
        ("-2421341,454321", 404),
        ("e", 404),
        ("englishstring", 404),
        ("с", 404),
        ("строканарусском", 404),
        ("*", 404),
        ("*&873%", 404),
    ],
)
class CatalogDynamicTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_item_detail(self):
        url = f"/catalog/{self.number}/"
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, self.status, f"{self.number} failed"
        )

    def test_item_detail_re(self):
        url = f"/catalog/re/{self.number}/"
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, self.status, f"{self.number} failed"
        )

    def test_custom_converter(self):
        url = f"/catalog/converter/{self.number}/"
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, self.status, f"{self.number} failed"
        )


class CatalogDynamicUniqueTests(TestCase):
    def setUp(self):
        self.client = Client()

    @parameterized.expand([("0", 200)])
    def test_item_detail_unique(self, number, status):
        url = f"/catalog/{number}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status, f"{number} failed")

    @parameterized.expand([("0", 404)])
    def test_item_detail_re_unique(self, number, status):
        url = f"/catalog/re/{number}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status, f"{number} failed")

    @parameterized.expand([("0", 404)])
    def test_custom_converter_unique(self, number, status):
        url = f"/catalog/converter/{number}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status, f"{number} failed")


class CatalogStaticTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_item_list(self):
        response = self.client.get(reverse("item_list"))
        self.assertEqual(response.status_code, 200)


class ItemModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = Category.objects.create(
            name="Куртки",
            is_published=True,
            slug="kurtki",
            weight=5000,
        )
        cls.tag = Tag.objects.create(
            name="Женская коллекция",
            is_published=True,
            slug="women",
        )

    def test_item_create(self):
        item_count = Item.objects.count()
        self.item = Item(
            name="Кроссовки",
            is_published=True,
            text="Кроссовки для бега мужские."
            " Роскошно подойдут для бега по утрам",
            category=self.category,
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(
            Item.objects.count(),
            item_count + 1,
        )

    def test_unable_create_one_letter(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(
                name="Кроссовки",
                is_published=True,
                text="К",
                category=self.category,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(
            Item.objects.count(),
            item_count,
        )

    def test_unable_create_without_adverbs(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(
                name="Кроссовки",
                is_published=True,
                text="Кроссовки для бега мужские.",
                category=self.category,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(
            Item.objects.count(),
            item_count,
        )

    def test_unable_create_big_name(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(
                name="Кроссовки" + "*" * 150,
                is_published=True,
                text="Кроссовки для бега мужские. "
                "Роскошно подойдут для бега по утрам",
                category=self.category,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(
            Item.objects.count(),
            item_count,
        )


class TagModelTests(TestCase):
    def test_tag_create(self):
        item_count = Tag.objects.count()

        self.tag = Tag(
            name="Женская коллекция",
            is_published=True,
            slug="women-collection",
        )
        self.tag.full_clean()
        self.tag.save()

        self.assertEqual(
            Tag.objects.count(),
            item_count + 1,
        )

    def test_unable_create_tag_big_name(self):
        item_count = Tag.objects.count()
        with self.assertRaises(ValidationError):
            self.tag = Tag(
                name="Женская коллекция" + "*" * 150,
                is_published=True,
                slug="women-collection",
            )
            self.tag.full_clean()
            self.tag.save()
        self.assertEqual(
            Tag.objects.count(),
            item_count,
        )

    def test_unable_create_tag_wrong_slug(self):
        item_count = Tag.objects.count()
        with self.assertRaises(ValidationError):
            self.tag = Tag(
                name="Женская коллекция",
                is_published=True,
                slug="женская",
            )
            self.tag.full_clean()
            self.tag.save()
        self.assertEqual(
            Tag.objects.count(),
            item_count,
        )


class CategoryModelTests(TestCase):
    def test_category_create(self):
        category_count = Category.objects.count()

        self.category = Category(
            name="Обувь",
            is_published=True,
            slug="obuv",
            weight=2000,
        )
        self.category.full_clean()
        self.category.save()

        self.assertEqual(
            Category.objects.count(),
            category_count + 1,
        )

    def test_unable_create_category_big_name(self):
        item_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = Category(
                name="Обувь" + "*" * 150,
                is_published=True,
                slug="obuv",
                weight=2000,
            )
            self.category.full_clean()
            self.category.save()
        self.assertEqual(
            Category.objects.count(),
            item_count,
        )

    def test_unable_create_category_wrong_slug(self):
        item_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = Category(
                name="Обувь",
                is_published=True,
                slug="обувь",
                weight=2000,
            )
            self.category.full_clean()
            self.category.save()
        self.assertEqual(
            Category.objects.count(),
            item_count,
        )

    def test_unable_create_category_wrong_weight1(self):
        item_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = Category(
                name="Обувь",
                is_published=True,
                slug="обувь",
                weight=-100,
            )
            self.category.full_clean()
            self.category.save()
        self.assertEqual(
            Category.objects.count(),
            item_count,
        )

    def test_unable_create_category_wrong_weight2(self):
        item_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = Category(
                name="Обувь",
                is_published=True,
                slug="обувь",
                weight=32768,
            )
            self.category.full_clean()
            self.category.save()
        self.assertEqual(
            Category.objects.count(),
            item_count,
        )
