import core.models

import django.core.exceptions
import django.core.validators
import django.db.models


def exist_adverbs_validator(value):
    if not ("превосходно" in value.lower() or "роскошно" in value.lower()):
        raise django.core.exceptions.ValidationError(
            "Не содержит наречий. Добавьте `превосходно` или `роскошно`"
        )


class Item(core.models.AbstractModel):
    text = django.db.models.TextField(
        validators=[exist_adverbs_validator],
        verbose_name="Описание",
        help_text="Придумайте описание. Текст должен включать"
        " слова превосходно или роскошно",
    )
    category = django.db.models.ForeignKey(
        "category",
        on_delete=django.db.models.CASCADE,
        verbose_name="Категория",
        help_text="Выберите категорию или добавьте новую",
    )
    tags = django.db.models.ManyToManyField(
        "tag",
        verbose_name="Теги",
        help_text="Выберите тег или создайте новый",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Tag(core.models.AbstractModelWithSlug):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(core.models.AbstractModelWithSlug):
    weight = django.db.models.IntegerField(
        default=100,
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(32767),
        ],
        verbose_name="Масса",
        help_text="Укажите массу",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
