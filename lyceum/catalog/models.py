import catalog.validators

import core.models

import django.core.validators
import django.db.models


class Item(core.models.NameFieldMixin, core.models.IsPublishedFieldMixin):
    text = django.db.models.TextField(
        validators=[catalog.validators.exist_adverbs_validator],
        verbose_name="описание",
        help_text="Придумайте описание. Текст должен включать"
        " слова превосходно или роскошно",
    )
    category = django.db.models.ForeignKey(
        "category",
        on_delete=django.db.models.CASCADE,
        verbose_name="категория",
        help_text="Выберите категорию или добавьте новую",
    )
    tags = django.db.models.ManyToManyField(
        "tag",
        verbose_name="теги",
        help_text="Выберите тег или создайте новый",
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class Tag(
    core.models.NameFieldMixin,
    core.models.IsPublishedFieldMixin,
    core.models.SlugFieldMixin,
):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class Category(
    core.models.NameFieldMixin,
    core.models.IsPublishedFieldMixin,
    core.models.SlugFieldMixin,
):
    weight = django.db.models.IntegerField(
        default=100,
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(32767),
        ],
        verbose_name="масса",
        help_text="Укажите массу",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
