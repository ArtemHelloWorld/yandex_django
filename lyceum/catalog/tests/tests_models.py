import catalog.models

from django.core.exceptions import ValidationError
from django.test import TestCase


class ItemModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = catalog.models.Category.objects.create(
            name="Куртки",
            is_published=True,
            slug="kurtki",
            weight=5000,
        )
        cls.tag = catalog.models.Tag.objects.create(
            name="Женская коллекция",
            is_published=True,
            slug="women",
        )

    def tearDown(self):
        catalog.models.Item.objects.all().delete()
        super(ItemModelTests, self).tearDown()

    def test_item_create(self):
        item_count = catalog.models.Item.objects.count()
        self.item = catalog.models.Item(
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
            catalog.models.Item.objects.count(),
            item_count + 1,
        )

    def test_unable_create_one_letter(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = catalog.models.Item(
                name="Кроссовки",
                is_published=True,
                text="К",
                category=self.category,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count,
        )

    def test_unable_create_without_adverbs(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = catalog.models.Item(
                name="Кроссовки",
                is_published=True,
                text="Кроссовки для бега мужские.",
                category=self.category,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count,
        )

    def test_unable_create_big_name(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = catalog.models.Item(
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
            catalog.models.Item.objects.count(),
            item_count,
        )


class TagModelTests(TestCase):
    def tearDown(self):
        catalog.models.Tag.objects.all().delete()
        super(TagModelTests, self).tearDown()

    def test_tag_create(self):
        item_count = catalog.models.Tag.objects.count()

        self.tag = catalog.models.Tag(
            name="Женская коллекция",
            is_published=True,
            slug="women-collection",
        )
        self.tag.full_clean()
        self.tag.save()

        self.assertEqual(
            catalog.models.Tag.objects.count(),
            item_count + 1,
        )

    def test_unable_create_tag_big_name(self):
        item_count = catalog.models.Tag.objects.count()
        with self.assertRaises(ValidationError):
            self.tag = catalog.models.Tag(
                name="Женская коллекция" + "*" * 150,
                is_published=True,
                slug="women-collection",
            )
            self.tag.full_clean()
            self.tag.save()
        self.assertEqual(
            catalog.models.Tag.objects.count(),
            item_count,
        )

    def test_unable_create_tag_wrong_slug(self):
        item_count = catalog.models.Tag.objects.count()
        with self.assertRaises(ValidationError):
            self.tag = catalog.models.Tag(
                name="Женская коллекция",
                is_published=True,
                slug="женская",
            )
            self.tag.full_clean()
            self.tag.save()
        self.assertEqual(
            catalog.models.Tag.objects.count(),
            item_count,
        )


class CategoryModelTests(TestCase):
    def tearDown(self):
        catalog.models.Category.objects.all().delete()
        super(CategoryModelTests, self).tearDown()

    def test_category_create(self):
        category_count = catalog.models.Category.objects.count()

        self.category = catalog.models.Category(
            name="Обувь",
            is_published=True,
            slug="obuv",
            weight=2000,
        )
        self.category.full_clean()
        self.category.save()

        self.assertEqual(
            catalog.models.Category.objects.count(),
            category_count + 1,
        )

    def test_unable_create_category_big_name(self):
        item_count = catalog.models.Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = catalog.models.Category(
                name="Обувь" + "*" * 150,
                is_published=True,
                slug="obuv",
                weight=2000,
            )
            self.category.full_clean()
            self.category.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            item_count,
        )

    def test_unable_create_category_wrong_slug(self):
        item_count = catalog.models.Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = catalog.models.Category(
                name="Обувь",
                is_published=True,
                slug="обувь",
                weight=2000,
            )
            self.category.full_clean()
            self.category.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            item_count,
        )

    def test_unable_create_category_wrong_weight1(self):
        item_count = catalog.models.Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = catalog.models.Category(
                name="Обувь",
                is_published=True,
                slug="обувь",
                weight=-100,
            )
            self.category.full_clean()
            self.category.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            item_count,
        )

    def test_unable_create_category_wrong_weight2(self):
        item_count = catalog.models.Category.objects.count()
        with self.assertRaises(ValidationError):
            self.category = catalog.models.Category(
                name="Обувь",
                is_published=True,
                slug="обувь",
                weight=32768,
            )
            self.category.full_clean()
            self.category.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            item_count,
        )
